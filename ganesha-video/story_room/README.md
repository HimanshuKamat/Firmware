# The Story Room

A small team that turns a one-line idea from the human owner into an approved script, ready for the production pipeline (keyframes, clips, voice, music, graphics, edit). It exists to do the part that most decides whether a children's video is good: **the idea, the shape of the story, and what the child does while watching.**

The human is always the Idea Owner and the final approver. The agents argue, research and draft; the human decides at four gates.

## Who is in the room

| Role | Who | What they do | Brief |
|---|---|---|---|
| **Idea Owner** | the human | Gives the idea, picks the direction, approves each gate | n/a |
| **Facilitator** | the main agent (the only one who talks to the human) | Runs the session, asks sharp questions, shows 2 to 3 options with a recommendation, keeps the decision log | `roles/facilitator.md` |
| **Trend Scout** | sub-agent | Market and format intelligence for this specific idea: gap, season, title and thumbnail angles, policy risks | `roles/trend_scout.md` |
| **Movement and Engagement Designer** | sub-agent | Designs what the child does: movement, counting, call-and-response, pauses, energy curve, seated alternatives | `roles/movement_designer.md` |
| **Cultural and Values Advisor** | sub-agent | Accuracy, variants between traditions, what to soften, pronunciation list, what a human family reviewer must check | `roles/cultural_advisor.md` |
| **Scriptwriter** | sub-agent | Writes the beat sheet, then the script, only after the concept is locked | `roles/scriptwriter.md` |
| **Critic Panel** | 4 fresh-context sub-agents | Try to break the script: toddler reader, engagement auditor, production-feasibility and cost, respect and safety | `roles/critic_panel.md` |

Why the Facilitator is the main agent: sub-agents cannot talk to the human. One voice keeps the conversation simple and the creative direction consistent. The specialists give input; they do not make the decisions.

## The four gates

```
IDEA (human, any form: a sentence, a festival, a movement, a character, a moral)
  |
  v
STAGE 1  SPARK        Trend Scout + Movement Designer + Cultural Advisor work in parallel;
                      Facilitator adds 3 to 5 story angles          -> Spark Sheet
  GATE 1  human picks or mixes an angle (and says what they like / dislike)
  |
  v
STAGE 2  CONCEPT      Facilitator drafts a one-page concept: logline, lesson, cast, places,
                      interaction map, movement map, song or chant idea, length, cost estimate
  GATE 2  human locks the concept        (nothing is scripted before this)
  |
  v
STAGE 3  BEAT SHEET   Scriptwriter writes 15 to 25 beats with interaction and energy markers;
                      Critic Panel reviews; Facilitator merges fixes
  GATE 3  human approves the beats
  |
  v
STAGE 4  SCRIPT       Scriptwriter writes the full script in the project format, with 2
                      alternative openings and 2 endings; Critic Panel reviews; fixes applied
  GATE 4  human approves the script      -> hand over to production (same as Checkpoint 1)
```

Rules at every gate: at most three options, always one recommendation with the reason, plain language, one decision at a time. The Facilitator records every decision in `projects/<slug>/decisions.md` and never reopens a decision unless the human does.

## What makes this different from "just ask for a script"

1. **Evidence first.** Market trends, child-engagement research and movement design are gathered before writing (`research/`, summarised in `playbook.md`).
2. **The child's job is designed, not sprinkled on.** Every beat says what the child sees, hears and does.
3. **Written for the production pipeline.** The Production-Feasibility critic checks beat lengths, cast size, shots a video model may refuse, text-in-frame hazards, lip-sync needs, and gives a credit estimate before any credits are spent (lessons from the first film, `PROJECT_REVIEW_REPORT.txt`).
4. **Independent critics.** The people who wrote the script do not judge it.
5. **Respect is a gate, not an afterthought.** The Cultural Advisor reports before the concept is locked.

## How to start

Say, in any words: "Story Room: my idea is ...". Even "Diwali, with a lot of clapping" is enough. The Facilitator replies with a short list of questions only if something essential is missing (audience age, length, festival date, a person or character that must appear), otherwise it goes straight to the Spark.

## Files

```
story_room/
  README.md              this file
  playbook.md            the research distilled into rules and numbers (written from research/)
  research/              market_trends, engagement_science, movement_design, format_teardown,
                         story_bank, script_craft (each with a verification log)
  roles/                 the seven role briefs (used as the prompt for each sub-agent)
  templates/             idea_brief, spark_sheet, concept_one_pager, beat_sheet, script_template
  projects/<slug>/       one folder per film: idea.md, spark_sheet.md, concept.md, beats.md,
                         script.md, critic_reports/, decisions.md
```

The skill `/story-room` (in `.claude/skills/story-room/`) loads this process into a session.

## Boundaries

- No credits are spent in the Story Room. Web research is free; generation tools are not used.
- Approved scripts are copied to `01_script/` of the production project and become read-only, as before.
- The Story Room never decides on its own that a religious or cultural detail is correct. It flags it for a human family reviewer.
