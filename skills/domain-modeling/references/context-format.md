# CONTEXT.md format

## Structure

```md
# {Context name}

{One or two sentences describing what this context covers and why it exists.}

## Language

**Order**:
A confirmed customer request for one or more line items.
_Avoid_: Purchase, transaction

**Invoice**:
A payment request issued to a customer after fulfillment.
_Avoid_: Bill, receipt

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account
```

## Rules

- **Pick one canonical term.** When multiple words refer to the same concept, choose one canonical name and list rejected synonyms under `_Avoid_`.
- **Keep definitions tight.** Use one or two sentences that define what the concept is, not how the code implements it.
- **Include only domain-specific concepts.** Exclude general programming terms such as retry policies, caches, or HTTP handlers.
- **Group terms under subheadings.** Use subheadings when natural clusters emerge, and otherwise keep a flat list.

## Single vs multi-context repositories

- **Single context.** Maintain one `<main-repo>/.agent-docs/CONTEXT.md` file.
- **Multiple contexts.** Maintain `<main-repo>/.agent-docs/CONTEXT-MAP.md` listing each bounded context, its dictionary path, and how contexts relate:

```md
# Context map

## Contexts

- [Ordering](contexts/ordering.md): receives and tracks customer orders
- [Billing](contexts/billing.md): generates invoices and processes payments
- [Fulfillment](contexts/fulfillment.md): manages warehouse picking and shipping

## Relationships

- **Ordering -> Fulfillment**: Ordering emits `OrderPlaced` events consumed by Fulfillment.
- **Fulfillment -> Billing**: Fulfillment emits `ShipmentDispatched` events consumed by Billing.
- **Ordering <-> Billing**: Share `CustomerId` and `Money` value types.
```

Infer which structure applies:

- If `.agent-docs/CONTEXT-MAP.md` exists, read it to locate the relevant context file.
- If `.agent-docs/CONTEXT.md` exists, use the single-context structure.
- If neither exists, create `<main-repo>/.agent-docs/CONTEXT.md` lazily when the first term is resolved.
