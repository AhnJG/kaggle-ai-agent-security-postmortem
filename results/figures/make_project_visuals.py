"""Build the README's four project visuals from documented facts and the curated CSV.

This renders an archive; it does not run attacks, models, or competition submissions.
Leaderboard values are a dated snapshot, distinct from owner-entered row scores.
"""

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
WIDTH = 1440
INK = "#182632"
MUTED = "#52616e"
LINE = "#dce3e8"
PALE = "#f5f7f9"
BLUE = "#24618b"
RED = "#9b414b"
TEAL = "#276c62"
SNAPSHOT = {"checked": "2026-10-11", "public": 93.835, "private": 0.000,
            "public_rank": 223, "private_rank": 3231}

plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none",
                     "svg.hashsalt": "agent-security-postmortem", "font.size": 15})


def records():
    with (ROOT / "results/submissions.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    numeric = []
    for row in rows:
        if not row["public_score"] and not row["private_score"]:
            continue
        if not row["public_score"] or not row["private_score"]:
            raise ValueError(f"Incomplete score pair: {row['submission']}")
        row = dict(row)
        for key in ("public_score", "private_score"):
            row[key] = float(row[key])
            if not math.isfinite(row[key]):
                raise ValueError(f"Non-finite score: {row['submission']}")
        numeric.append(row)
    by_name = {row["submission"]: row for row in numeric}
    finalists = [by_name[name] for name in ("method39_broad_per-model_race", "v27_adapt")]
    if any(row["final_selected"] != "yes" for row in finalists):
        raise ValueError("The visual's two named finalists no longer match the curated flags")
    successful = [row for row in numeric if row["status"] == "Succeeded"]
    exfil = [row for row in successful if row["family"] == "exfiltration"]
    deputy = [row for row in successful if row["family"] == "confused_deputy"]
    if not exfil or any(row["private_score"] != 0 for row in exfil):
        raise ValueError("EXFILTRATION observation changed; revise the narrative")
    if not deputy or any(row["private_score"] != row["public_score"] for row in deputy):
        raise ValueError("CONFUSED_DEPUTY observation changed; revise the narrative")
    best = max(numeric, key=lambda row: row["private_score"])
    if best["submission"] != "v11_deputy_transfer" or best["final_selected"] == "yes":
        raise ValueError("The best-Private comparison changed; revise the narrative")
    return {"rows": rows, "numeric": numeric, "finalists": finalists,
            "best": best, "exfil": exfil, "deputy": deputy}


def canvas(height):
    fig = plt.figure(figsize=(WIDTH / 100, height / 100), dpi=100, facecolor="white")
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set(xlim=(0, WIDTH), ylim=(height, 0))
    ax.axis("off")
    fig.text_constraints = []
    return fig, ax


def text(ax, x, y, content, size=15, color=INK, weight="normal", width=None):
    artist = ax.text(x, y, content, fontsize=size, color=color, weight=weight,
                     ha="left", va="top", linespacing=1.35)
    ax.figure.text_constraints.append((artist, width or WIDTH - x - 50, content))
    return artist


def box(ax, x, y, w, h, fill=PALE, edge=LINE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=9",
                               facecolor=fill, edgecolor=edge, linewidth=1))


def arrow(ax, start, end, color=MUTED, dashed=False):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13,
                                color=color, linewidth=1.2,
                                linestyle="--" if dashed else "-"))


def header(ax, section, title, subtitle):
    text(ax, 60, 36, section, 11.5, BLUE, "bold")
    text(ax, 60, 66, title, 27, weight="bold")
    text(ax, 60, 119, subtitle, 14, MUTED)


def save(fig, stem, title, description):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    scale = fig.axes[0].bbox.width / WIDTH
    issues = []
    for artist, allowed, content in fig.text_constraints:
        if artist.get_window_extent(renderer).width > allowed * scale + 1:
            issues.append(f"column overflow: {content!r}")
        bounds = artist.get_window_extent(renderer)
        if bounds.x0 < 0 or bounds.x1 > fig.bbox.width or bounds.y0 < 0 or bounds.y1 > fig.bbox.height:
            issues.append(f"canvas overflow: {content!r}")
    if issues:
        raise ValueError(f"Layout issues in {stem}: " + "; ".join(issues))
    fig.savefig(HERE / f"{stem}.png", dpi=150,
                metadata={"Title": title, "Description": description})
    fig.savefig(HERE / f"{stem}.svg",
                metadata={"Title": title, "Description": description, "Date": None,
                          "Creator": "Team Sian / project visual generator"})
    plt.close(fig)


def overview(data):
    fig, ax = canvas(900)
    header(ax, "KAGGLE  /  TEAM SIAN  /  PROJECT OVERVIEW",
           "When the visible score did not transfer",
           "AI Agent Security: tool-use red-teaming in a fixture-backed competition sandbox.")
    metrics = [
        ("OFFICIAL PUBLIC", f"{SNAPSHOT['public']:.3f}", f"Rank {SNAPSHOT['public_rank']:,}", BLUE),
        ("OFFICIAL PRIVATE", f"{SNAPSHOT['private']:.3f}", f"Final rank {SNAPSHOT['private_rank']:,}", RED),
        ("CURATED RECORD", str(len(data["rows"])), f"rows / {len(data['numeric'])} numeric score pairs", INK),
    ]
    for i, (label, value, note, color) in enumerate(metrics):
        x = 60 + i * 448
        box(ax, x, 166, 424, 138)
        text(ax, x + 24, 183, label, 11.5, MUTED, "bold", 376)
        text(ax, x + 24, 212, value, 34, color, "bold", 376)
        text(ax, x + 24, 269, note, 14, MUTED, width=376)
    text(ax, 60, 332, "METHOD IN BRIEF", 11.5, BLUE, "bold")
    steps = [
        ("Public materials", "Notebooks, SDK,\nand discussions"),
        ("Adapt variants", "Candidate selection,\nbudgets, diagnostics"),
        ("Check evidence", "Local checks\nHosted Public scores"),
        ("Select finalists", "Two recorded picks\nfrom EXFILTRATION"),
        ("Private outcome", "Both recorded picks\nreturned 0 points"),
    ]
    for i, (title, body) in enumerate(steps):
        x = 60 + i * 268
        box(ax, x, 364, 244, 144, fill="white")
        text(ax, x + 18, 381, f"0{i + 1}", 11.5, BLUE if i < 4 else RED, "bold", 208)
        text(ax, x + 18, 407, title, 16, weight="bold", width=208)
        text(ax, x + 18, 445, body, 13.5, MUTED, width=208)
        if i < 4:
            arrow(ax, (x + 249, 435), (x + 263, 435))
    text(ax, 60, 531, "Contribution: public-code adaptation, diagnostic integration, variant comparisons, and evidence review.",
         14.5, MUTED)
    text(ax, 60, 578, "LESSONS", 11.5, BLUE, "bold")
    lessons = [
        ("Carry uncertainty forward", "Hidden-defense risk was discussed;\nfinal selection still concentrated\nin one attack family."),
        ("Respect evidence layers", "Local checks and Public scores\ndo not establish Private transfer\nor explain the cause of a gain."),
        ("Preserve corrections", "Invalid metrics were withdrawn.\nKeep corrections and their evidence\nwith the experiment record."),
    ]
    for i, (title, body) in enumerate(lessons):
        x = 60 + i * 448
        box(ax, x, 610, 424, 168)
        text(ax, x + 22, 632, title, 17, weight="bold", width=380)
        text(ax, x + 22, 673, body, 14, MUTED, width=380)
    text(ax, 60, 807, "Leaderboard snapshot: 2026-10-11. Individual Private scores and selection flags are owner-maintained records.",
         11.5, MUTED)
    text(ax, 60, 836, "Private scores were hidden during the contest. Benchmark outcomes do not establish effectiveness on real systems.",
         11.5, MUTED)
    save(fig, "project_overview", "AI Agent Security project overview",
         "Benchmark context, official results, research flow, contribution, and retrospective lessons.")


def workflow():
    fig, ax = canvas(1000)
    header(ax, "01  /  METHODOLOGY", "From community inputs to a submission decision",
           "A retrospective reconstruction of the work; it is not an identical protocol for every historical run.")
    lanes = [
        ("PUBLIC STARTING POINTS", "Live-fill and prompt-format ideas\nLocal-runtime setup references\nSDK behavior; attribution in NOTICE"),
        ("OWNER'S WORK", "Adaptation and integration\nBudget / candidate-selection variants\nExperiments and evidence review"),
        ("CODING-AGENT SUPPORT", "Implementation, planning, and review\nOwner directed the work and\nmade final submission decisions"),
    ]
    for i, (label, body) in enumerate(lanes):
        x = 60 + 448 * i
        box(ax, x, 171, 424, 132)
        text(ax, x + 22, 188, label, 11, BLUE, "bold", 380)
        text(ax, x + 22, 218, body, 14, MUTED, width=380)
    stages = [
        ("Hypothesis", "Define the candidate\nand intended change"),
        ("Implementation", "Adapt code, budget,\nand selection logic"),
        ("Local checks", "Syntax and behavior\nProxy measurements"),
        ("Public scoring", "Hosted score records\nVariant comparisons"),
        ("Final selection", "method39 and\nv27_adapt"),
    ]
    for i, (title, body) in enumerate(stages):
        x = 60 + 268 * i
        box(ax, x, 353, 244, 166, fill="white")
        text(ax, x + 18, 373, f"0{i + 1}", 11.5, BLUE, "bold", 208)
        text(ax, x + 18, 405, title, 16, weight="bold", width=208)
        text(ax, x + 18, 447, body, 13.5, MUTED, width=208)
        if i < 4:
            arrow(ax, (x + 249, 436), (x + 263, 436))
    # Iteration is a feedback relationship, not a claimed chronological event count.
    ax.plot([986, 986, 450], [522, 558, 558], color=MUTED, linewidth=1, linestyle="--")
    arrow(ax, (450, 558), (450, 522), dashed=True)
    text(ax, 454, 574, "Revise variants and hypotheses", 13, MUTED, width=535)
    arrow(ax, (1254, 522), (1254, 545), RED)
    box(ax, 1064, 551, 336, 89, fill="#fbf3f4", edge="#e8cdd1")
    text(ax, 1083, 566, "PRIVATE: AFTER SELECTION", 10.5, RED, "bold", 298)
    text(ax, 1083, 595, "0.000 points / rank 3,231", 13, RED, width=298)
    text(ax, 60, 672, "WHAT EACH EVIDENCE LAYER CAN SUPPORT", 11.5, BLUE, "bold")
    layers = [
        ("local_gguf", "Syntax, branches,\nrough local behavior", "Cannot establish\nhosted performance."),
        ("cm391 board-like proxy", "Candidate compression\ninside the proxy runtime", "Can disagree with Kaggle;\nuse behavior checks after mismatch."),
        ("Kaggle Public score", "Observed hosted score\nin that evaluation", "Cannot establish Private transfer\nor isolate a causal improvement."),
    ]
    for i, (title, supports, limit) in enumerate(layers):
        x = 60 + 448 * i
        box(ax, x, 705, 424, 216)
        text(ax, x + 22, 726, title, 17, weight="bold", width=380)
        text(ax, x + 22, 770, supports, 14, MUTED, width=380)
        text(ax, x + 22, 845, limit, 13, RED, width=380)
    text(ax, 60, 950, "Later rules formalized artifact hashes and decision criteria; they do not prove universal preregistration. See docs/agentic_research_workflow.md.",
         10.5, MUTED)
    save(fig, "research_workflow", "Research workflow and evidence layers",
         "Attributed inputs, owner work, agent support, iterative experiments, and limits of local, proxy, and Public evidence.")


def outcomes(data):
    fig, ax = canvas(940)
    header(ax, "02  /  RECORDED RESULTS", "The final picks and an unselected alternative",
           "Scores are aggregate benchmark points, not success percentages. These row scores come from the curated CSV.")
    for x, color, label in ((480, BLUE, "Public"), (670, RED, "Private")):
        ax.scatter([x], [179], s=95, color=color, zorder=5)
        text(ax, x + 18, 168, label, 14, color, width=150)
    xscore = lambda value: 480 + 8.5 * value
    selected = data["finalists"]
    comparisons = [
        (selected[0], "method39", "Recorded final selection"),
        (selected[1], "v27_adapt", "Recorded final selection"),
        (data["best"], "v11_deputy_transfer", "Highest recorded Private; unselected"),
    ]
    for i, (row, title, note) in enumerate(comparisons):
        y = 266 + 126 * i
        text(ax, 60, y - 20, title, 18, weight="bold", width=365)
        text(ax, 60, y + 17, note, 12.5, MUTED, width=365)
        public, private = row["public_score"], row["private_score"]
        ax.plot([xscore(private), xscore(public)], [y, y], color=LINE, linewidth=3, zorder=1)
        ax.scatter([xscore(public)], [y], s=230, facecolors="white", edgecolors=BLUE, linewidths=2.4, zorder=4)
        ax.scatter([xscore(private)], [y], s=90, color=RED, zorder=5)
        if public == private:
            text(ax, xscore(public) - 73, y - 42, f"{public:.3f} / {private:.3f}", 14, TEAL, "bold", 250)
        else:
            text(ax, xscore(public) - 29, y - 42, f"{public:.3f}", 15, BLUE, "bold", 140)
            text(ax, xscore(private) - 29, y + 19, f"{private:.3f}", 15, RED, "bold", 140)
    ax.plot([xscore(0), xscore(100)], [598, 598], color=LINE, linewidth=1)
    for value in range(0, 101, 20):
        ax.plot([xscore(value)] * 2, [598, 605], color=MUTED, linewidth=1)
        text(ax, xscore(value) - 9, 615, str(value), 12, MUTED, width=50)
    text(ax, 1168, 654, "Benchmark score", 12, MUTED, width=212)
    text(ax, 60, 691, "OBSERVATIONS IN SUCCESSFUL ROWS OF THE CURATED TABLE", 11.5, BLUE, "bold")
    box(ax, 60, 721, 648, 112)
    box(ax, 732, 721, 648, 112)
    text(ax, 82, 744, str(len(data["exfil"])), 29, RED, "bold", 92)
    text(ax, 184, 743, "EXFILTRATION rows: Private 0\nA pattern in these records;\nhidden mechanism unknown.",
         13, MUTED, width=498)
    text(ax, 754, 744, str(len(data["deputy"])), 29, TEAL, "bold", 60)
    text(ax, 822, 743, "CONFUSED_DEPUTY rows: equal scores\nRetrospective equality;\ntransfer is not guaranteed.",
         13, MUTED, width=532)
    text(ax, 60, 865, "Private scores were entered manually; selection flags were not independently matched to original Kaggle submission IDs.",
         11.5, MUTED)
    text(ax, 60, 894, "This comparison does not establish rerun scores, causal superiority, or a counterfactual medal. Source: results/submissions.csv.",
         11.5, MUTED)
    save(fig, "selection_outcomes", "Recorded final selections and Private outcomes",
         "Public and Private scores for the two flagged finalists and the highest recorded Private alternative, with provenance limits.")


def lessons():
    fig, ax = canvas(990)
    header(ax, "03  /  RETROSPECTIVE LESSONS", "Lessons for the next experiment",
           "Recommendations drawn from this case; they are not claims of a universally effective strategy.")
    rows = [
        ("Carry uncertainty into selection",
         "Hidden-defense risk was discussed.\nThe recorded finalists still concentrated\nin EXFILTRATION and both had Private 0.",
         "Compare failure mechanisms before selection.\nRecord what supports transfer and what\nremains unknown; diversification is not a guarantee."),
        ("Separate an observed score from its cause",
         "method39 had the highest recorded Public score.\nUnmatched historical variants do not isolate\nthe effect of routing, speed, or individual edits.",
         "Set the comparison and decision rule before a run.\nUse matched comparisons when feasible;\nkeep Public feedback as secondary evidence."),
        ("Validate metrics and keep their corrections",
         "The September 2 correction withdrew\ninvalid timeout_free_n and unique_cells\ninterpretations from a local probe.",
         "Define metrics against the actual measurement.\nPreserve invalid runs and corrected interpretations.\nSeparate code failure, proxy mismatch, and strategy."),
    ]
    for i, (title, observed, change) in enumerate(rows):
        y = 185 + 229 * i
        box(ax, 60, y, 1320, 203)
        text(ax, 83, y + 20, f"0{i + 1}", 18, BLUE, "bold", 48)
        text(ax, 137, y + 20, title, 20, weight="bold", width=1219)
        text(ax, 137, y + 70, "OBSERVATION", 10.5, MUTED, "bold", 548)
        text(ax, 137, y + 97, observed, 13.5, MUTED, width=548)
        arrow(ax, (702, y + 132), (742, y + 132), BLUE)
        text(ax, 767, y + 70, "NEXT DECISION", 10.5, BLUE, "bold", 591)
        text(ax, 767, y + 97, change, 13.5, INK, width=591)
    text(ax, 60, 917, "Read the current interpretation in docs/postmortem.md and docs/hypotheses_ledger.md; the Korean log preserves historical claims and corrections.",
         10.5, MUTED)
    text(ax, 60, 946, "The archive provides selected artifacts, not complete hosted reproduction or proof of generalization beyond the competition sandbox.",
         11, MUTED)
    save(fig, "experiment_lessons", "Lessons for future experiment decisions",
         "Three observed issues connected to future selection, comparison, and measurement decisions, with explicit evidence boundaries.")


def main():
    data = records()
    overview(data)
    workflow()
    outcomes(data)
    lessons()
    print("Saved 4 project visuals in SVG and PNG; text widths and canvas bounds checked.")


if __name__ == "__main__":
    main()
