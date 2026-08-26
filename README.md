<div align="center">

<img src="assets/header-banner.gif" width="100%"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=500&size=22&duration=3000&pause=1000&color=7C9CFF&center=true&vCenter=true&repeat=true&width=600&height=35&lines=AI+agents+that+grow+memory;AMP+%E2%80%94+Agent+Memory+Protocol;AMPS+%E2%80%94+Automations+%C2%B7+Muscles+%C2%B7+Protocols+%C2%B7+Scripts;Systems+that+build+systems;An+ecosystem+with+its+own+gravity)](https://git.io/typing-svg)

</div>

---

### `// WHO`

Builder of AI agent infrastructure. I design protocols and systems that let agents remember, orient, and grow without databases, embeddings, or cloud services. Just files.

**[Soma](https://soma.gravicity.ai)** is the agent. **[Somaverse](https://somaverse.ai)** is the ecosystem it lives in. The protocols below are the specs behind it — twelve open standards anyone can implement, born from production.

---

### `// NOW`

<!-- NOW:START -->
🔺 **[PRISM](https://github.com/curtismercier/prism)** is public — `v0.1.1`, spec + two reference renderers (a Node build-step and a browser custom element) developed in parallel as a *branching-cycle* and compared empirically. Actively in progress.<br/><br/>
📈 **[Soma](https://soma.gravicity.ai)** has passed **~6,800 [npm downloads](https://www.npmjs.com/package/meetsoma)** since first publish, peaking at **945/week in May 2026**. Found organically — built in the open, used by people I haven't met.<br/><br/>
🔁 **[Protocols](https://github.com/curtismercier/protocols)** at `family-v0.4` — Anti-Patterns and Conformance sections landed across all eleven specs. A spec you can *fail* is a spec you can implement.<br/><br/>
🧠 **[MLX](https://github.com/curtismercier/protocols/tree/main/mlx)** + **[MLR](https://github.com/curtismercier/protocols/tree/main/mlr)** v0.1 — the extraction/reflection pair. MLX audits before close: what's still floating that's not on disk? MLR catches it in flight.<br/><br/>
💧 **[Tincture v0.2.2](https://github.com/curtismercier/tincture)** — multi-axis design substrate extracted as standalone. Tokens are matrices, not pairs. A drop changes the whole pour.
<!-- NOW:END -->

---

## `// WHAT I'M BUILDING`

### 🌿 [Soma](https://soma.gravicity.ai)

**AI coding agent with memory.** Built on Pi. Identity discovery, session breathing, filesystem memory, AMPS-driven behavior. The agent that grows around you.

[![npm](https://img.shields.io/npm/dw/meetsoma?label=downloads&color=7C9CFF)](https://www.npmjs.com/package/meetsoma)
[![npm version](https://img.shields.io/npm/v/meetsoma?label=version&color=BC52EE)](https://www.npmjs.com/package/meetsoma)
[![License](https://img.shields.io/badge/license-BSL--1.1-blue)](https://github.com/meetsoma)

`TypeScript` · [meetsoma](https://github.com/meetsoma)

---

<table>
<tr>
<td width="50%" valign="top">

### 🔺 [PRISM](https://github.com/curtismercier/prism) <sub>`// IN PROGRESS`</sub>
**One source. Three projections.**

A document substrate where humans, agents, and tooling read the same Markdown surfaced differently. Section-anchored edits. No whole-file rereads. Two reference renderers in the repo — a Node build-step and a browser custom element — developed in parallel as a branching-cycle and being compared empirically.

`Spec + Reference impls` · `CC BY 4.0` + `MIT`

</td>
<td width="50%" valign="top">

### 💧 [Tincture](https://github.com/curtismercier/tincture)
**A drop changes the whole pour.**

Surface-aware, multi-axis design substrate for AI-mediated theming. One mood delta shifts an entire visual identity. Tokens are matrices, not pairs — their value depends on which axes are active.

`v0.2.2` · `Active` · Born from a production site that needed to mood-shift instantly

</td>
</tr>
</table>

---

## `// PROTOCOLS`

Twelve open specs for agent memory, architecture, and identity. Born from building Soma, published as standalone standards. All **CC BY 4.0**. Family-level milestones tagged (`family-v0.4` as of May 2026).

### Substrate

| | |
|---|---|
| **[AMP](https://github.com/curtismercier/protocols/tree/main/amp)** v0.3 | Agent Memory Protocol — filesystem-based persistent memory with heat tracking, preloads, checkpoints |
| **[AMPS](https://github.com/curtismercier/protocols/tree/main/amps)** v1.1 | Four content types over AMP: Automations, Muscles, Protocols, Scripts |
| **[MAPS](https://github.com/curtismercier/protocols/tree/main/maps)** v0.1 | Navigation layer over AMPS — task-specific paths through what an agent knows |

### Session lifecycle

| | |
|---|---|
| **[Breath Cycle](https://github.com/curtismercier/protocols/tree/main/breath-cycle)** v0.2 | Inhale → process → exhale → rest. Context depletion as design, not bug |
| **[PHASE](https://github.com/curtismercier/protocols/tree/main/phase)** v0.3 | Three-tier brain configuration (T1 prompt-config, T2 phase-folder convention, T3 runtime) + meta-orchestration cycle + delegation-owned worktrees |
| **[MLX](https://github.com/curtismercier/protocols/tree/main/mlx)** v0.1 | Memory Lane Xtraction — audit-before-close. What's still floating that's not on disk? |
| **[MLR](https://github.com/curtismercier/protocols/tree/main/mlr)** v0.1 | Mid-session Learning Review — in-flight catch. PAUSE → NAME → FILE → RESUME when a pattern emerges during work |

### Provenance & growth

| | |
|---|---|
| **[SEAMS](https://github.com/curtismercier/protocols/tree/main/seams)** v0.2 | Traceable connections between every artifact. Sessions trace time, documents trace space |
| **[SEEDS](https://github.com/curtismercier/protocols/tree/main/seeds)** v0.2 | Drop a seed in any folder; it tells the agent how to grow it |
| **[ATLAS](https://github.com/curtismercier/protocols/tree/main/atlas)** v0.2 | Living architecture maps. Accurate because they're the primary reference, not an afterthought |

### Identity & documents

| | |
|---|---|
| **[Identity](https://github.com/curtismercier/protocols/tree/main/identity)** v0.1 | Contextual identity discovery — agents that know who they are from where they are |
| **[PRISM](https://github.com/curtismercier/prism)** v0.1 | Document projection substrate (separate repo, sibling spec) — *in progress* |

---

## `// PHILOSOPHY`

<div align="center">

> Most frameworks treat agent memory as a retrieval problem — vector databases, embeddings, RAG.
>
> I think it's simpler than that. **The agent reads and writes files. Like a human with a notebook.**
>
> No infrastructure. No embeddings model. No cloud service. Just Markdown on disk.

<br/>

> The context window isn't a problem to solve. **It's a breath.**
>
> It fills, it empties, it fills again. An agent that knows it will forget is more capable than one that pretends it won't.

</div>

---

## `// ALSO`

- **[openclaw-mods](https://github.com/curtismercier/openclaw-mods)** — Community patches for OpenClaw: per-agent compaction, context management

---

## `// SHIPPING`

*Auto-pulled from public GitHub activity. Refreshes every 6 hours.*

<!-- HIGHLIGHTS:START -->
🏷️ Tagged [`v0.42.1`](https://github.com/meetsoma/soma-beta/releases/tag/v0.42.1) on `meetsoma/soma-beta` · <sub>2026-07-31</sub>

📦 Published [`meetsoma@0.31.0`](https://www.npmjs.com/package/meetsoma) to npm · <sub>2026-06-11</sub>

🏷️ Tagged [`v0.1.1`](https://github.com/curtismercier/prism/releases/tag/v0.1.1) on `curtismercier/prism` · <sub>2026-05-14</sub>

🏷️ Tagged [`family-v0.4`](https://github.com/curtismercier/protocols/releases/tag/family-v0.4) on `curtismercier/protocols` · <sub>2026-05-12</sub>

🏷️ Tagged [`skill-forge-v1.0.0`](https://github.com/curtismercier/skill-forge/releases/tag/skill-forge-v1.0.0) on `curtismercier/skill-forge` · <sub>2026-04-17</sub>

🌿 Created branch `feat/icon-pipeline` on `meetsoma/website`
<!-- HIGHLIGHTS:END -->

<details>
<summary><sub>other activity</sub></summary>

<!-- OTHER:START -->
⭐ Starred [`Anil-matcha/Open-Generative-AI`](https://github.com/Anil-matcha/Open-Generative-AI)

⭐ Starred [`harry0703/MoneyPrinterTurbo`](https://github.com/harry0703/MoneyPrinterTurbo)

⭐ Starred [`toeverything/AFFiNE`](https://github.com/toeverything/AFFiNE)

⭐ Starred [`semantica-agi/semantica`](https://github.com/semantica-agi/semantica)

⭐ Starred [`Kitsun3Sec/Pentest-Cheat-Sheets`](https://github.com/Kitsun3Sec/Pentest-Cheat-Sheets)

⭐ Starred [`devanshbatham/FavFreak`](https://github.com/devanshbatham/FavFreak)

⭐ Starred [`qaz69s/panda-zig`](https://github.com/qaz69s/panda-zig)

⭐ Starred [`block/buzz`](https://github.com/block/buzz)
<!-- OTHER:END -->

</details>

---

## `// STACK`

<div align="center">

![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=claude&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Astro](https://img.shields.io/badge/Astro-BC52EE?style=for-the-badge&logo=astro&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SurrealDB](https://img.shields.io/badge/SurrealDB-FF00A0?style=for-the-badge&logo=surrealdb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

<div align="center">

**[soma.gravicity.ai](https://soma.gravicity.ai)** · **[somaverse.ai](https://somaverse.ai)** · **[gravicity.ai](https://gravicity.ai)**

<sub>Systems that build systems.</sub>

</div>
