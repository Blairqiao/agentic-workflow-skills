---
name: unslop
description: >-
  Cut AI tells, empty corporate buzzwords, excessive hedging, and boilerplate from any writing, specs, plans, proofs, walkthroughs, or code comments. Must always apply.
---

# Unslop

Edit authored prose and comments to remove AI patterns. Never alter fenced code blocks, terminal command output, logs, commit hashes, file paths, or verbatim quotes. Apply these rules to both user-facing documentation and internal workflow artifacts in `.agent-docs/`.

## Process

1. Scan authored prose and comments for the patterns below, skipping code blocks and verbatim evidence.
2. Rewrite to preserve meaning and match the intended tone.
3. Run a self-audit asking what makes the text read like AI output, and fix any remaining tells.

## Patterns to detect and fix

### Content

- **Superficial -ing phrases.** Cut or expand trailing participles like "highlighting...", "ensuring...", "reflecting...", "showcasing...", or "fostering..." with concrete facts.
- **Vague attributions.** Replace "Experts believe", "Industry reports suggest", or "Some critics argue" with specific sources, or delete them.

### Language

- **AI vocabulary.** Replace words like additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, abstract uses of landscape, pivotal, showcase, abstract uses of tapestry, testament, underscore, and vibrant with plain words.
- **Fancy ways to say "is".** Replace "serves as", "stands as", "boasts", or "features" with "is" or "has".
- **Contrast clichés.** Avoid "Not just X, but Y" framing. State the point directly.
- **Rule of three.** Do not force ideas into groups of three. Use the natural number of items.
- **Synonym cycling.** Do not cycle through synonyms like protagonist, main character, central figure, and hero in one paragraph. Pick one canonical term and repeat it.
- **False ranges.** Avoid "from X to Y" where X and Y do not sit on a meaningful scale. List the topics directly.

### Style

- **Em dash overuse.** Avoid em dashes entirely. Use periods or commas only, with no parentheses, no en dashes, and no hyphen-as-dash substitutes in prose. If a thought needs separation, end the sentence or use a comma.
- **Colon overuse.** Colons belong before a list or example, not as mid-sentence connectors. Rewrite comparison framing so the sentence stands on its own.
- **Boldface overuse.** Do not bold every proper noun or acronym.
- **Inline-header lists.** Avoid a bold label and colon that restates the line, such as "**Performance:** Performance improved...". Convert those to prose, or use a bold lead-in that ends in a period, names the item, and is followed by new detail, such as "**Schema in TypeScript.** Tables live in one file."
- **Title case headings.** Use sentence case for all Markdown headings.
- **Decorative emojis.** Remove emojis from headings, bullets, and prompts.
- **Curly quotes.** Replace typographic curly quotes with straight quotes.

### Communication artifacts

- **Chatbot phrases.** Remove filler like "I hope this helps!", "Let me know if...", "Of course!", "Certainly!", or "Found the smoking gun!".
- **Sycophantic tone.** Skip openings like "Great question! You're absolutely right!" and respond directly.

### Filler

- **Filler phrases.** Shorten "In order to" to "To" and "Due to the fact that" to "Because". Delete "It is important to note that".
- **Excessive hedging.** Replace stacked qualifiers like "might potentially", "could possibly", or "tends to suggest" with direct statements or explicit conditions.
