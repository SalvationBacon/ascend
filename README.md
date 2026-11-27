# Ascend

A personal level-up fitness tracker. Clear your Daily Quest, earn XP, raise your stats and climb from E-Rank to S-Rank. Skip a day and a Penalty Quest shows up.

It's one self-contained file: `index.html`. No build step, no dependencies, no account.

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

## Running it

Open `index.html` in a browser, or host it with GitHub Pages (Settings → Pages → deploy from `main`).

## Where your data lives

- **Opened as a Claude artifact:** progress syncs to your Claude account, and the AI coach and AI-generated Gates work.
- **Opened anywhere else** (a local file, GitHub Pages): progress is saved in that browser's local storage. The AI features show as unavailable. Use **System → Copy backup** to move your save between devices.
