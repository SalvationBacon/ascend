# Ascend

A personal level-up fitness tracker. Clear your Daily Quest, earn XP, raise your stats and climb from E-Rank to S-Rank. Skip a day and a Penalty Quest shows up.

**Live app:** https://salvationbacon.github.io/ascend/

## Install it on your phone

- **iPhone (Safari):** open the link, tap **Share**, then **Add to Home Screen**.
- **Android (Chrome):** open the link, then tap **Install app** in the banner or the ⋮ menu. You can also use **System → Install app** inside Ascend.

Once installed, it opens full screen with its own icon and works offline.

## Features

- **Daily Quest**: pick from 8 exercises (push-ups, sit-ups, squats, run, plank, pull-ups, burpees, steps), with a countdown to midnight.
- **Scaling**: targets grow 2% per level up to 2× at level 51, then 1% per level up to 3× at level 151.
- **Penalty Quest**: issued if you miss a day. It scales with your level, and XP is halved until you clear it.
- **Ranks E to S**: Rank Trials at levels 10, 20, 35, 50 and 70 (double your daily targets in one session).
- **Stats**: STR, AGI, VIT, SEN and INT, plus 3 free points every level.
- **Side Quests**: your own daily habits, each tagged to a stat.
- **Gates**: harder optional workouts that unlock by rank.
- **Weekly Boss**: one of six rotating bosses, fought on weekends.
- **Job Change at level 40**: Pathfinder, Juggernaut, Brawler or Ascetic.
- **Body tracking**: weight and measurements, with a trend chart.
- **17 titles**, a 15-week calendar, lifetime totals and a rest timer.
- **Auto difficulty**: suggests moving up a difficulty after 14 cleared days in a row.
- **Backup**: copy your whole save as text and restore it on any device.

## Where your data lives

- **Web app (GitHub Pages):** saved in that browser's storage on your phone. Use **System → Copy backup** now and then, and paste the text somewhere safe. If you clear site data or switch phones, **Restore backup** brings it back.
- **Claude artifact version:** syncs to your Claude account. The AI coach and AI-generated Gates only work there.

## Files

| File | What it is |
|---|---|
| `app.html` | The app's source. Edit this one. It's also what the Claude artifact publishes. |
| `index.html` | The installable web app, **generated** from `app.html`. Don't edit by hand. |
| `manifest.webmanifest` | App name, colors and icons for installing. |
| `sw.js` | Service worker that makes it work offline. |
| `icons/` | `icon.svg` is the source art; the PNGs are generated from it. |
| `tools/build.py` | Rebuilds `index.html` and updates the service worker version. |
| `tools/make-icons.js` | Renders the PNG icons from `icons/icon.svg` (needs Playwright). |

After changing `app.html`:

```sh
python3 tools/build.py
```

After changing `icons/icon.svg`:

```sh
node tools/make-icons.js
```
