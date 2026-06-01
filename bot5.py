<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AVIACOM — Rocket to Riches</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600;700&display=swap" rel="stylesheet">
<script src="https://js.paystack.co/v1/inline.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="https://accounts.google.com/gsi/client" async defer></script>
<script>
  // Initialize EmailJS immediately when script loads
  window.addEventListener('load', function() {
    emailjs.init("u4u854Rh1Q9p5OY52");
  });
</script>
<style>
:root {
  --bg: #080808;
  --card: #111111;
  --card2: #161616;
  --border: rgba(255,100,0,0.2);
  --orange: #FF6600;
  --orange2: #FF4400;
  --orange3: #FF9900;
  --text: #F0F0F0;
  --muted: #666;
  --green: #00FF88;
  --red: #FF2244;
  --gold: #FFD700;
}
* { margin:0; padding:0; box-sizing:border-box; }
html, body { height:100%; overflow-x:hidden; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Rajdhani', sans-serif;
  min-height: 100vh;
}

/* ── BACKGROUND ── */
.bg-grid {
  position: fixed; inset: 0; z-index: 0;
  background-image:
    linear-gradient(rgba(255,102,0,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,102,0,0.04) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
}
.bg-glow {
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background: radial-gradient(ellipse 60% 40% at 50% 0%, rgba(255,100,0,0.12) 0%, transparent 70%);
}

/* ── PAGES ── */
.page { display:none; position:relative; z-index:1; min-height:100vh; }
.page.active { display:block; }

/* ── NAV ── */
nav {
  display: flex; align-items: center; justify-content: space-between;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid var(--border);
  background: rgba(8,8,8,0.9);
  backdrop-filter: blur(10px);
  position: sticky; top: 0; z-index: 100;
}
.logo {
  font-family: 'Orbitron', sans-serif;
  font-size: 1.4rem; font-weight: 900;
  color: var(--orange);
  letter-spacing: 2px;
  text-shadow: 0 0 20px rgba(255,102,0,0.5);
}
.logo span { color: var(--text); }

/* ── BUTTONS ── */
.btn {
  padding: .6rem 1.4rem; border: none; border-radius: 6px;
  font-family: 'Rajdhani', sans-serif; font-weight: 700;
  font-size: .9rem; cursor: pointer; transition: all .2s; letter-spacing: 1px;
}
.btn-orange {
  background: linear-gradient(135deg, var(--orange), var(--orange2));
  color: #fff;
  box-shadow: 0 4px 20px rgba(255,102,0,0.4);
}
.btn-orange:hover { transform: translateY(-1px); box-shadow: 0 6px 28px rgba(255,102,0,0.6); }
.btn-outline {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text);
}
.btn-outline:hover { border-color: var(--orange); color: var(--orange); }
.btn-green {
  background: linear-gradient(135deg, #00cc66, #00FF88);
  color: #000; font-weight: 900;
  box-shadow: 0 4px 20px rgba(0,255,136,0.3);
}
.btn-green:hover { transform: translateY(-2px); box-shadow: 0 6px 30px rgba(0,255,136,0.5); }
.btn-red {
  background: linear-gradient(135deg, #cc0022, var(--red));
  color: #fff;
  box-shadow: 0 4px 20px rgba(255,34,68,0.3);
}
.btn-full { width: 100%; padding: .85rem; font-size: 1rem; }
.btn-sm { padding: .4rem .9rem; font-size: .8rem; }
.btn:disabled { opacity: .4; cursor: not-allowed; transform: none !important; }

/* ── LANDING ── */
.hero {
  text-align: center;
  padding: 5rem 1.5rem 3rem;
}
.hero h1 {
  font-family: 'Orbitron', sans-serif;
  font-size: clamp(2.5rem, 8vw, 5rem);
  font-weight: 900;
  line-height: 1;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--orange3), var(--orange), var(--orange2));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  text-shadow: none;
  filter: drop-shadow(0 0 30px rgba(255,102,0,0.4));
}
.hero p {
  font-size: 1.15rem; color: var(--muted); max-width: 480px; margin: 0 auto 2.5rem;
  line-height: 1.6;
}
.hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }

/* ── LIVE TICKER ── */
.live-ticker {
  background: var(--card); border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  padding: .6rem 1.5rem;
  display: flex; align-items: center; gap: 1rem; overflow: hidden;
}
.ticker-label {
  font-family: 'Orbitron', sans-serif; font-size: .65rem;
  color: var(--orange); letter-spacing: 2px; white-space: nowrap;
  background: rgba(255,102,0,0.1); padding: .3rem .6rem; border-radius: 4px;
}
.ticker-inner { display: flex; gap: 1.5rem; animation: ticker 20s linear infinite; }
.ticker-item { white-space: nowrap; font-size: .85rem; color: var(--muted); }
.ticker-item span { color: var(--green); font-weight: 700; }
@keyframes ticker { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }

/* ── FEATURES ── */
.features {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem; padding: 2rem 1.5rem;
}
.feat {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 12px; padding: 1.5rem;
}
.feat-icon { font-size: 2rem; margin-bottom: .75rem; }
.feat h3 { font-family: 'Orbitron', sans-serif; font-size: .85rem; color: var(--orange); margin-bottom: .5rem; }
.feat p { font-size: .9rem; color: var(--muted); line-height: 1.5; }

/* ── MODALS ── */
.modal-bg {
  display: none; position: fixed; inset: 0; z-index: 1000;
  background: rgba(0,0,0,0.85); backdrop-filter: blur(8px);
  align-items: center; justify-content: center; padding: 1rem;
}
.modal-bg.open { display: flex; }
.modal {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 16px; padding: 2rem; width: 100%; max-width: 420px;
  max-height: 92vh; overflow-y: auto; position: relative;
}
.modal h2 {
  font-family: 'Orbitron', sans-serif; font-size: 1.1rem;
  color: var(--orange); margin-bottom: .4rem; letter-spacing: 2px;
}
.modal p { color: var(--muted); font-size: .9rem; margin-bottom: 1.5rem; }
.modal-close {
  position: absolute; top: 1rem; right: 1rem;
  background: none; border: none; color: var(--muted);
  font-size: 1.2rem; cursor: pointer;
}
.modal-close:hover { color: var(--orange); }

/* ── FORM ── */
.form-group { margin-bottom: 1rem; }
.form-group label { display: block; font-size: .8rem; color: var(--muted); margin-bottom: .4rem; letter-spacing: 1px; }
.form-group input, .form-group select {
  width: 100%; padding: .75rem 1rem;
  background: var(--card2); border: 1px solid var(--border);
  border-radius: 8px; color: var(--text);
  font-family: 'Rajdhani', sans-serif; font-size: .95rem;
  transition: border-color .2s;
}
.form-group input:focus, .form-group select:focus {
  outline: none; border-color: var(--orange);
}
.form-group select option { background: var(--card2); }

/* ── GAME PAGE ── */
#gamePage { background: var(--bg); }

.game-nav-info {
  display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap;
}
.balance-chip {
  background: rgba(255,102,0,0.1); border: 1px solid var(--border);
  border-radius: 8px; padding: .35rem .85rem;
  font-family: 'Orbitron', sans-serif; font-size: .75rem;
  color: var(--orange);
}
.balance-chip span { color: var(--text); font-size: .9rem; }

/* ── GAME AREA ── */
.game-layout {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 1rem;
  padding: 1rem 1.5rem;
  min-height: calc(100vh - 65px);
}
@media(max-width:700px) {
  .game-layout { grid-template-columns: 1fr; }
}

/* ── ROCKET CANVAS ── */
.game-panel {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 16px; overflow: hidden; position: relative;
}
#rocketCanvas { width: 100%; display: block; background: transparent; }

.multiplier-display {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  text-align: center; pointer-events: none;
}
.multiplier-display .mult {
  font-family: 'Orbitron', sans-serif;
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 900;
  line-height: 1;
  transition: color .1s;
}
.multiplier-display .mult.flying { color: var(--orange3); text-shadow: 0 0 40px rgba(255,153,0,0.6); }
.multiplier-display .mult.crashed { color: var(--red); text-shadow: 0 0 40px rgba(255,34,68,0.6); }
.multiplier-display .mult.waiting { color: var(--muted); }
.multiplier-display .status {
  font-size: .85rem; letter-spacing: 3px; color: var(--muted); margin-top: .3rem;
}

.crash-label {
  position: absolute; top: 1rem; left: 50%; transform: translateX(-50%);
  font-family: 'Orbitron', sans-serif; font-size: .7rem; letter-spacing: 2px;
  background: rgba(255,34,68,0.15); border: 1px solid rgba(255,34,68,0.3);
  color: var(--red); padding: .3rem .8rem; border-radius: 20px;
  display: none;
}

/* ── LIVE BETS PANEL ── */
.side-panel { display: flex; flex-direction: column; gap: 1rem; }
.panel-box {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 16px; padding: 1.25rem; flex-shrink: 0;
}
.panel-box h3 {
  font-family: 'Orbitron', sans-serif; font-size: .7rem;
  color: var(--orange); letter-spacing: 2px; margin-bottom: 1rem;
}

/* ── BET CONTROLS ── */
.bet-row { display: flex; gap: .5rem; align-items: center; margin-bottom: .75rem; }
.bet-input {
  flex: 1; padding: .65rem .9rem;
  background: var(--card2); border: 1px solid var(--border);
  border-radius: 8px; color: var(--text);
  font-family: 'Orbitron', sans-serif; font-size: .9rem;
}
.bet-input:focus { outline: none; border-color: var(--orange); }
.quick-bets { display: flex; gap: .4rem; flex-wrap: wrap; margin-bottom: .75rem; }
.qb {
  padding: .3rem .6rem; background: var(--card2); border: 1px solid var(--border);
  border-radius: 6px; font-size: .75rem; color: var(--muted);
  cursor: pointer; transition: all .2s; font-family: 'Rajdhani';
}
.qb:hover { border-color: var(--orange); color: var(--orange); }

.auto-row {
  display: flex; align-items: center; gap: .75rem; margin-bottom: .75rem;
  font-size: .85rem; color: var(--muted);
}
.auto-row input[type=checkbox] { accent-color: var(--orange); width:14px; height:14px; }
.auto-cashout-val {
  width: 70px; padding: .35rem .5rem;
  background: var(--card2); border: 1px solid var(--border);
  border-radius: 6px; color: var(--orange);
  font-family: 'Orbitron'; font-size: .8rem; text-align: center;
}

/* ── LIVE BETS LIST ── */
.bets-list { max-height: 220px; overflow-y: auto; }
.bet-item {
  display: flex; justify-content: space-between; align-items: center;
  padding: .45rem 0; border-bottom: 1px solid rgba(255,102,0,0.08);
  font-size: .82rem;
}
.bet-item:last-child { border: none; }
.bet-user { color: var(--muted); }
.bet-amount { color: var(--text); font-weight: 600; }
.bet-mult { font-family: 'Orbitron'; font-size: .75rem; }
.bet-mult.won { color: var(--green); }
.bet-mult.lost { color: var(--red); }
.bet-mult.live { color: var(--orange); animation: pulse 1s infinite; }

/* ── HISTORY ── */
.hist-list { display: flex; flex-wrap: wrap; gap: .4rem; }
.hist-chip {
  padding: .25rem .6rem; border-radius: 20px; font-size: .75rem;
  font-family: 'Orbitron'; font-weight: 700;
}
.hist-chip.low { background: rgba(0,255,136,0.1); color: var(--green); border: 1px solid rgba(0,255,136,0.2); }
.hist-chip.mid { background: rgba(255,102,0,0.1); color: var(--orange); border: 1px solid rgba(255,102,0,0.2); }
.hist-chip.high { background: rgba(255,34,68,0.1); color: var(--red); border: 1px solid rgba(255,34,68,0.2); }

/* ── TOAST ── */
.toast {
  position: fixed; bottom: 2rem; left: 50%; transform: translateX(-50%);
  background: var(--card); border: 1px solid var(--orange);
  color: var(--text); padding: .75rem 1.5rem; border-radius: 30px;
  font-size: .9rem; z-index: 9999; opacity: 0;
  transition: opacity .3s; pointer-events: none; text-align: center;
  max-width: 90vw;
}
.toast.show { opacity: 1; }

/* ── TABS ── */
.tabs { display: flex; gap: 0; margin-bottom: 1rem; border-radius: 8px; overflow: hidden; border: 1px solid var(--border); }
.tab {
  flex: 1; padding: .6rem; text-align: center;
  background: var(--card2); color: var(--muted);
  cursor: pointer; font-size: .8rem; letter-spacing: 1px;
  transition: all .2s; border: none; font-family: 'Rajdhani'; font-weight: 600;
}
.tab.active { background: var(--orange); color: #fff; }

/* ── STATS ── */
.stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: .75rem; }
.stat-box {
  background: var(--card2); border: 1px solid var(--border);
  border-radius: 10px; padding: 1rem; text-align: center;
}
.stat-box .val {
  font-family: 'Orbitron'; font-size: 1.2rem; color: var(--orange); font-weight: 700;
}
.stat-box .lbl { font-size: .75rem; color: var(--muted); margin-top: .3rem; letter-spacing: 1px; }

/* ── ANIMATIONS ── */
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }
@keyframes shake { 0%,100%{transform:translateX(0)} 25%{transform:translateX(-8px)} 75%{transform:translateX(8px)} }
@keyframes fadeIn { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
.shake { animation: shake .4s; }
.fade-in { animation: fadeIn .4s ease; }

/* ── DEPOSIT/WITHDRAW ── */
.dw-tabs { display:flex; gap:.5rem; margin-bottom:1rem; }
.dw-tab {
  flex:1; padding:.6rem; border-radius:8px; border:1px solid var(--border);
  background:var(--card2); color:var(--muted); cursor:pointer;
  font-family:'Rajdhani'; font-weight:700; font-size:.9rem; text-align:center;
}
.dw-tab.active { background:var(--orange); color:#fff; border-color:var(--orange); }

/* ── REFERRAL ── */
.ref-box {
  background: var(--card2); border: 1px solid var(--border);
  border-radius: 10px; padding: 1rem; word-break: break-all;
  font-size: .8rem; color: var(--orange); margin-bottom: 1rem;
  font-family: 'Orbitron';
}
.ref-stats { display:grid; grid-template-columns:1fr 1fr; gap:.75rem; margin-top:1rem; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--card); }
::-webkit-scrollbar-thumb { background: var(--orange); border-radius: 2px; }

/* ── VERIFICATION ── */
.otp-inputs { display:flex; gap:.5rem; justify-content:center; margin:1rem 0; }
.otp-inputs input {
  width:48px; height:52px; text-align:center;
  background:var(--card2); border:1.5px solid var(--border);
  border-radius:8px; color:var(--orange);
  font-family:'Orbitron'; font-size:1.2rem; font-weight:700;
}
.otp-inputs input:focus { outline:none; border-color:var(--orange); }

/* ── GOOGLE BUTTON ── */
.btn-google {
  display: flex; align-items: center; justify-content: center; gap: .6rem;
  width: 100%; padding: .75rem; border-radius: 8px;
  background: #fff; color: #333; font-weight: 700;
  border: none; cursor: pointer; font-family: 'Rajdhani', sans-serif;
  font-size: .95rem; letter-spacing: .5px; transition: all .2s;
  margin-bottom: 1rem;
}
.btn-google:hover { background: #f0f0f0; transform: translateY(-1px); }
.btn-google img { width: 20px; height: 20px; }
.or-divider {
  display: flex; align-items: center; gap: .75rem;
  margin-bottom: 1rem; color: var(--muted); font-size: .8rem;
}
.or-divider::before, .or-divider::after {
  content: ''; flex: 1; height: 1px; background: var(--border);
}

/* ── MOBILE FIXES ── */
@media(max-width: 600px) {
  /* Nav */
  nav { padding: .75rem 1rem; gap: .5rem; flex-wrap: nowrap; }
  .logo { font-size: 1.1rem; }
  .game-nav-info { gap: .4rem; flex-wrap: wrap; justify-content: flex-end; }
  .game-nav-info .balance-chip { font-size: .65rem; padding: .3rem .5rem; }
  .game-nav-info .btn { padding: .35rem .6rem; font-size: .7rem; }

  /* Hero */
  .hero { padding: 2.5rem 1rem 2rem; }
  .hero h1 { font-size: 2.8rem; }
  .hero p { font-size: 1rem; }
  .hero-btns { flex-direction: column; align-items: stretch; gap: .75rem; }
  .hero-btns .btn { width: 100%; padding: .9rem; font-size: 1rem; }

  /* Landing nav buttons */
  #landingNav .btn { padding: .45rem .9rem; font-size: .8rem; }

  /* Features grid - 1 column */
  .features { grid-template-columns: 1fr; padding: 1rem; gap: .75rem; }
  .feat { padding: 1rem; }

  /* Game layout - stack vertically */
  .game-layout { padding: .5rem; gap: .75rem; }

  /* Rocket canvas smaller on mobile */
  #rocketCanvas { height: 260px !important; }
  .multiplier-display .mult { font-size: 2.8rem; }

  /* Side panel horizontal scroll on mobile */
  .side-panel { display: flex; flex-direction: column; gap: .75rem; }
  .panel-box { padding: 1rem; }

  /* Bet controls */
  .bet-row { flex-wrap: wrap; }
  .bet-input { min-width: 0; }
  .quick-bets { gap: .3rem; }
  .qb { padding: .35rem .55rem; font-size: .72rem; }

  /* History chips wrap nicely */
  .hist-list { gap: .3rem; }
  .hist-chip { font-size: .65rem; padding: .2rem .5rem; }

  /* Modal full screen on mobile */
  .modal-bg { padding: 0; align-items: flex-end; }
  .modal {
    border-radius: 20px 20px 0 0;
    max-height: 95vh;
    padding: 1.5rem 1.25rem;
  }

  /* OTP inputs smaller */
  .otp-inputs input { width: 40px; height: 46px; font-size: 1rem; }

  /* Wallet stats */
  .stat-grid { gap: .5rem; }
  .stat-box { padding: .75rem .5rem; }
  .stat-box .val { font-size: 1rem; }

  /* Referral */
  .ref-box { font-size: .7rem; }

  /* Live ticker */
  .live-ticker { padding: .5rem 1rem; }

  /* Win modal */
  #winModal .modal { border-radius: 20px 20px 0 0; }
}

@media(max-width: 380px) {
  .hero h1 { font-size: 2.2rem; }
  .otp-inputs input { width: 34px; height: 40px; font-size: .9rem; gap: .3rem; }
  .otp-inputs { gap: .3rem; }
  .game-nav-info { flex-wrap: wrap; justify-content: flex-end; gap: .3rem; }
  .game-nav-info .btn-sm { padding: .3rem .5rem; font-size: .65rem; display: inline-block !important; }
  .balance-chip { width: 100%; text-align: center; }
}
  background:var(--card2); border:1px solid var(--border); border-radius:8px;
  padding:.75rem; max-height:140px; overflow-y:auto;
  font-size:.8rem; color:var(--muted); line-height:1.6; margin-bottom:1rem;
}
.check-row { display:flex; align-items:center; gap:.6rem; font-size:.85rem; color:var(--muted); margin-bottom:1rem; }
.check-row input { accent-color:var(--orange); width:15px; height:15px; flex-shrink:0; }

.section-divider {
  text-align:center; color:var(--muted); font-size:.75rem; letter-spacing:2px;
  margin: 2rem 0 1rem; position:relative;
}
.section-divider::before {
  content:''; position:absolute; left:0; top:50%;
  width:100%; height:1px; background:var(--border);
}
.section-divider span { background:var(--card); padding:0 1rem; position:relative; }
</style>
</head>
<body>
<div class="bg-grid"></div>
<div class="bg-glow"></div>

<!-- ═══════════════════ LANDING ═══════════════════ -->
<div id="landingPage" class="page active">
  <nav>
    <div class="logo">AVIA<span>COM</span></div>
    <div id="landingNav" style="display:flex;gap:.6rem">
      <button class="btn btn-outline btn-sm" onclick="openModal('loginModal')">LOG IN</button>
      <button class="btn btn-orange btn-sm" onclick="openModal('signupModal')">SIGN UP</button>
    </div>
  </nav>

  <div class="live-ticker">
    <div class="ticker-label">🔴 LIVE</div>
    <div class="ticker-inner" id="tickerInner"></div>
  </div>

  <div class="hero">
    <h1>RIDE THE<br>ROCKET</h1>
    <p>Deposit, bet, watch the multiplier soar. Cash out before it crashes — or lose it all. Ghana's most thrilling game.</p>
    <div class="hero-btns" id="heroBtns">
      <button class="btn btn-orange" onclick="openModal('signupModal')">🚀 PLAY NOW — FREE</button>
      <button class="btn btn-outline" onclick="openModal('loginModal')">I HAVE AN ACCOUNT</button>
    </div>
  </div>

  <div class="features">
    <div class="feat"><div class="feat-icon">🚀</div><h3>INSTANT MULTIPLIERS</h3><p>Watch the rocket soar from 1.00x to 100x+ in seconds. Cash out at the perfect moment.</p></div>
    <div class="feat"><div class="feat-icon">💸</div><h3>REAL GHS PAYOUTS</h3><p>Withdraw winnings instantly to MTN, Vodafone, AirtelTigo or your bank account.</p></div>
    <div class="feat"><div class="feat-icon">👥</div><h3>REFER & EARN FOREVER</h3><p>Earn 2% of every win your friends make — for life. Plus bonus on their first deposit.</p></div>
    <div class="feat"><div class="feat-icon">🤖</div><h3>AUTO CASHOUT</h3><p>Set your target multiplier and let Aviacom cash out automatically. Never miss a win.</p></div>
    <div class="feat"><div class="feat-icon">🔒</div><h3>SECURE PAYMENTS</h3><p>Powered by Paystack. All deposits and withdrawals fully encrypted and verified.</p></div>
    <div class="feat"><div class="feat-icon">📊</div><h3>PROVABLY FAIR</h3><p>Every crash result is cryptographically generated. The game cannot be rigged.</p></div>
  </div>

  <div style="text-align:center;padding:1rem 1.5rem 3rem">
    <div class="terms-box" style="max-width:600px;margin:0 auto;text-align:left">
      <strong style="color:var(--orange)">AVIACOM TERMS & CONDITIONS</strong><br><br>
      1. You must be 18+ to play. Gambling can be addictive — play responsibly.<br>
      2. Minimum deposit: GHS 5. Minimum bet: GHS 2. Maximum bet: GHS 2,000.<br>
      3. Minimum withdrawal: GHS 20. Withdrawals processed within 24–48 hours.<br>
      4. House edge: 10% applied to all bets. Results are provably fair.<br>
      5. Referral commission: 2% of every win your referral makes, for life.<br>
      6. Referral first-deposit bonus: 5% of referral's first deposit credited to you.<br>
      7. Abuse of bonuses, bots, or multiple accounts will result in permanent ban.<br>
      8. Aviacom reserves the right to suspend accounts under investigation.<br>
      9. All disputes are final after 48 hours of the relevant game round.<br>
      10. By playing you agree to all terms above.
    </div>
  </div>
</div>

<!-- ═══════════════════ GAME PAGE ═══════════════════ -->
<div id="gamePage" class="page">
  <nav>
    <div class="logo">AVIA<span>COM</span></div>
    <div class="game-nav-info">
      <div class="balance-chip">BAL: GHS <span id="balDisplay">0.00</span></div>
      <button class="btn btn-orange btn-sm" onclick="openModal('depositModal')">+ DEPOSIT</button>
      <button class="btn btn-outline btn-sm" onclick="openModal('walletModal')">WALLET</button>
      <button class="btn btn-outline btn-sm" onclick="openModal('referModal')">REFER</button>
      <button class="btn btn-outline btn-sm" onclick="doLogout()">EXIT</button>
    </div>
  </nav>

  <div class="game-layout">
    <!-- LEFT: ROCKET PANEL -->
    <div class="game-panel">
      <canvas id="rocketCanvas" height="400"></canvas>
      <div class="multiplier-display">
        <div class="mult waiting" id="multDisplay">1.00x</div>
        <div class="status" id="statusDisplay">WAITING FOR NEXT ROUND</div>
      </div>
      <div class="crash-label" id="crashLabel">🚀 FLEW AWAY!</div>
    </div>

    <!-- RIGHT: CONTROLS + INFO -->
    <div class="side-panel">
      <!-- BET PANEL -->
      <div class="panel-box">
        <h3>PLACE BET</h3>
        <div class="tabs">
          <button class="tab active" onclick="switchBetTab(0)">BET 1</button>
          <button class="tab" onclick="switchBetTab(1)">BET 2</button>
        </div>

        <!-- BET 1 -->
        <div id="betPanel0">
          <div class="bet-row">
            <input class="bet-input" type="number" id="betAmt0" value="5" min="2" max="2000" placeholder="GHS">
            <button class="btn btn-outline btn-sm" onclick="halveBet(0)">½</button>
            <button class="btn btn-outline btn-sm" onclick="doubleBet(0)">2×</button>
          </div>
          <div class="quick-bets">
            <div class="qb" onclick="setBet(0,5)">5</div>
            <div class="qb" onclick="setBet(0,10)">10</div>
            <div class="qb" onclick="setBet(0,20)">20</div>
            <div class="qb" onclick="setBet(0,50)">50</div>
            <div class="qb" onclick="setBet(0,100)">100</div>
          </div>
          <div class="auto-row">
            <input type="checkbox" id="autoOn0" onchange="toggleAuto(0)">
            <label for="autoOn0">Auto cashout at</label>
            <input class="auto-cashout-val" type="number" id="autoVal0" value="2.00" step="0.1" min="1.1">x
          </div>
          <button class="btn btn-green btn-full" id="betBtn0" onclick="placeBet(0)">BET GHS 5</button>
          <button class="btn btn-red btn-full" id="cashBtn0" onclick="cashOut(0)" style="display:none;margin-top:.5rem">CASH OUT</button>
        </div>
      </div>

      <!-- CRASH HISTORY -->
      <div class="panel-box">
        <h3>CRASH HISTORY</h3>
        <div class="hist-list" id="histList"></div>
      </div>

      <!-- LIVE BETS -->
      <div class="panel-box" style="flex:1">
        <h3>LIVE BETS — <span id="liveCount">0</span> PLAYERS</h3>
        <div class="bets-list" id="betsList"></div>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════ MODALS ═══════════════ -->

<!-- SIGNUP -->
<div class="modal-bg" id="signupModal">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('signupModal')">✕</button>
    <h2>JOIN AVIACOM</h2>
    <p>Create your account and start playing instantly</p>
    <div id="signupStep1">
      <button class="btn-google" onclick="googleSignIn()">
        <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" alt="G">
        Continue with Google
      </button>
      <div class="or-divider"><span>OR SIGN UP WITH EMAIL</span></div>
      <div class="form-group"><label>FULL NAME</label><input type="text" id="su-name" placeholder="Your full name"></div>
      <div class="form-group"><label>EMAIL ADDRESS</label><input type="email" id="su-email" placeholder="you@email.com"></div>
      <div class="form-group"><label>PHONE (for withdrawals)</label><input type="tel" id="su-phone" placeholder="024 XXX XXXX"></div>
      <div class="form-group"><label>PASSWORD</label><input type="password" id="su-pass" placeholder="Min 6 characters"></div>
      <div class="form-group"><label>REFERRAL CODE (optional)</label><input type="text" id="su-ref" placeholder="Enter referral code"></div>
      <div class="form-group"><label>TELEGRAM USERNAME (optional — for notifications)</label><input type="text" id="su-tg" placeholder="@yourusername"></div>
      <div class="terms-box">
        You must be 18+ to play. Minimum bet GHS 2, maximum GHS 2,000. House edge 10%. Withdrawals minimum GHS 20. Referral commission 2% of wins for life. By signing up you accept all terms.
      </div>
      <div class="check-row"><input type="checkbox" id="su-terms"><label for="su-terms">I am 18+ and accept the Terms & Conditions</label></div>
      <button class="btn btn-orange btn-full" onclick="doSignupStep1()">CREATE ACCOUNT</button>
      <div style="text-align:center;margin-top:1rem;font-size:.85rem;color:var(--muted)">Already have an account? <a onclick="closeModal('signupModal');openModal('loginModal')" style="color:var(--orange);cursor:pointer">Log in</a></div>
    </div>
    <div id="signupStep2" style="display:none">
      <p style="color:var(--text);margin-bottom:.5rem">We sent a 6-digit code to <span id="su-email-show" style="color:var(--orange)"></span></p>
      <p>Enter it below to verify your account.</p>
      <div class="otp-inputs">
        <input type="text" maxlength="1" class="otp-digit" id="otp0" oninput="otpNext(0)">
        <input type="text" maxlength="1" class="otp-digit" id="otp1" oninput="otpNext(1)">
        <input type="text" maxlength="1" class="otp-digit" id="otp2" oninput="otpNext(2)">
        <input type="text" maxlength="1" class="otp-digit" id="otp3" oninput="otpNext(3)">
        <input type="text" maxlength="1" class="otp-digit" id="otp4" oninput="otpNext(4)">
        <input type="text" maxlength="1" class="otp-digit" id="otp5" oninput="otpNext(5)">
      </div>
      <button class="btn btn-orange btn-full" onclick="verifyOTP()">VERIFY & CREATE ACCOUNT</button>
      <div style="text-align:center;margin-top:.75rem;font-size:.8rem;color:var(--muted)">
        Didn't get it? <a onclick="resendOTP()" style="color:var(--orange);cursor:pointer">Resend code</a>
      </div>
    </div>
  </div>
</div>

<!-- LOGIN -->
<div class="modal-bg" id="loginModal">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('loginModal')">✕</button>
    <h2>WELCOME BACK</h2>
    <p>Log in to continue playing</p>
    <button class="btn-google" onclick="googleSignIn()">
      <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" alt="G">
      Continue with Google
    </button>
    <div class="or-divider"><span>OR LOGIN WITH EMAIL</span></div>
    <div class="form-group"><label>EMAIL</label><input type="email" id="li-email" placeholder="you@email.com"></div>
    <div class="form-group"><label>PASSWORD</label><input type="password" id="li-pass" placeholder="Your password"></div>
    <button class="btn btn-orange btn-full" onclick="doLogin()">LOG IN</button>
    <div style="text-align:center;margin-top:1rem;font-size:.85rem;color:var(--muted)">No account? <a onclick="closeModal('loginModal');openModal('signupModal')" style="color:var(--orange);cursor:pointer">Sign up free</a></div>
  </div>
</div>

<!-- DEPOSIT -->
<div class="modal-bg" id="depositModal">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('depositModal')">✕</button>
    <h2>DEPOSIT FUNDS</h2>
    <p>Min GHS 5 · Powered by Paystack</p>
    <div class="form-group">
      <label>AMOUNT (GHS)</label>
      <input type="number" id="dep-amt" value="20" min="5" max="5000" placeholder="Enter amount">
    </div>
    <div class="quick-bets" style="margin-bottom:1rem">
      <div class="qb" onclick="document.getElementById('dep-amt').value=10">10</div>
      <div class="qb" onclick="document.getElementById('dep-amt').value=20">20</div>
      <div class="qb" onclick="document.getElementById('dep-amt').value=50">50</div>
      <div class="qb" onclick="document.getElementById('dep-amt').value=100">100</div>
      <div class="qb" onclick="document.getElementById('dep-amt').value=200">200</div>
      <div class="qb" onclick="document.getElementById('dep-amt').value=500">500</div>
    </div>
    <button class="btn btn-orange btn-full" onclick="doDeposit()">💳 PAY WITH PAYSTACK</button>
    <div style="font-size:.75rem;color:var(--muted);text-align:center;margin-top:.75rem">MoMo · Card · Bank Transfer accepted</div>
  </div>
</div>

<!-- WALLET (Withdraw) -->
<div class="modal-bg" id="walletModal">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('walletModal')">✕</button>
    <h2>WALLET</h2>
    <div class="stat-grid" style="margin-bottom:1.5rem">
      <div class="stat-box"><div class="val" id="wBal">0.00</div><div class="lbl">BALANCE (GHS)</div></div>
      <div class="stat-box"><div class="val" id="wTotalDep">0.00</div><div class="lbl">TOTAL DEPOSITED</div></div>
      <div class="stat-box"><div class="val" id="wTotalWon">0.00</div><div class="lbl">TOTAL WON</div></div>
      <div class="stat-box"><div class="val" id="wTotalWith">0.00</div><div class="lbl">TOTAL WITHDRAWN</div></div>
    </div>
    <h2 style="margin-bottom:.75rem">WITHDRAW</h2>
    <p>Min GHS 20 · Processed in 24–48hrs</p>
    <div class="dw-tabs">
      <div class="dw-tab active" onclick="switchWith(0)">MOBILE MONEY</div>
      <div class="dw-tab" onclick="switchWith(1)">BANK TRANSFER</div>
    </div>
    <div id="withMoMo">
      <div class="form-group"><label>NETWORK</label>
        <select id="w-network"><option>MTN Mobile Money</option><option>Vodafone Cash</option><option>AirtelTigo Money</option></select>
      </div>
      <div class="form-group"><label>PHONE NUMBER</label><input type="tel" id="w-phone" placeholder="024 XXX XXXX"></div>
    </div>
    <div id="withBank" style="display:none">
      <div class="form-group"><label>BANK NAME</label><input type="text" id="w-bank" placeholder="e.g. GCB Bank"></div>
      <div class="form-group"><label>ACCOUNT NUMBER</label><input type="text" id="w-acc" placeholder="Account number"></div>
      <div class="form-group"><label>ACCOUNT NAME</label><input type="text" id="w-accname" placeholder="Account holder name"></div>
    </div>
    <div class="form-group"><label>AMOUNT (GHS)</label><input type="number" id="w-amt" placeholder="Min GHS 20" min="20"></div>
    <button class="btn btn-orange btn-full" onclick="doWithdraw()">REQUEST WITHDRAWAL</button>
  </div>
</div>

<!-- REFERRAL -->
<div class="modal-bg" id="referModal">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('referModal')">✕</button>
    <h2>REFER & EARN</h2>
    <p>Earn 2% of every win your friends make — forever. Plus 5% of their first deposit.</p>
    <div style="font-size:.8rem;color:var(--muted);margin-bottom:.5rem;letter-spacing:1px">YOUR REFERRAL LINK</div>
    <div class="ref-box" id="refLinkBox">—</div>
    <div style="display:flex;gap:.5rem;margin-bottom:1.5rem;flex-wrap:wrap">
      <button class="btn btn-orange" onclick="copyRef()" style="flex:1">COPY LINK</button>
      <button class="btn btn-outline" onclick="shareWhatsApp()" style="flex:1">WHATSAPP</button>
      <button class="btn btn-outline" onclick="shareTelegram()" style="flex:1">TELEGRAM</button>
    </div>
    <div class="ref-stats">
      <div class="stat-box"><div class="val" id="refCount">0</div><div class="lbl">REFERRALS</div></div>
      <div class="stat-box"><div class="val" id="refEarned">0.00</div><div class="lbl">GHS EARNED</div></div>
    </div>
  </div>
</div>

<!-- WIN MODAL -->
<div class="modal-bg" id="winModal">
  <div class="modal" style="text-align:center">
    <h2 style="font-size:1.5rem;text-align:center">🚀 CASHED OUT!</h2>
    <div style="font-family:'Orbitron';font-size:3rem;color:var(--green);margin:1rem 0" id="winMultDisp">2.00x</div>
    <div style="font-size:1.1rem;color:var(--muted);margin-bottom:.5rem">YOU WON</div>
    <div style="font-family:'Orbitron';font-size:2rem;color:var(--gold)" id="winAmtDisp">GHS 10.00</div>
    <div style="font-size:.8rem;color:var(--muted);margin:1rem 0" id="winRefNote" style="display:none"></div>
    <button class="btn btn-orange btn-full" style="margin-top:1.5rem" onclick="closeModal('winModal')">KEEP PLAYING 🔥</button>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
// ══════════════════════════════════════════════════
//  CONFIG — REPLACE THESE WITH YOUR OWN VALUES
// ══════════════════════════════════════════════════
const SUPABASE_URL  = "https://bjgtbhjogbqtyrmpqhnm.supabase.co";
const SUPABASE_KEY  = "sb_publishable_TfT4M6Ttezj76PJJGhQ6mg_Oc26fJRB";
const sb = supabase.createClient(SUPABASE_URL, SUPABASE_KEY);

const PAYSTACK_KEY  = "pk_live_43a4e2c5203be6ae79d012694379691a2c129f89";
const EMAILJS_SVC   = "service_pl4kshn";
const EMAILJS_TPL   = "template_74chryr";
const EMAILJS_KEY   = "u4u854Rh1Q9p5OY52";
const TG_BOT_TOKEN  = "8805295472:AAEX198MM0mh4lTe4xdJ2vGB9Ml5B0XLYL8";
const TG_CHAT_ID    = "8162426062";
const HOUSE_EDGE    = 0.10; // 10%
const MIN_BET       = 2;
const MAX_BET       = 2000;
const MIN_WITHDRAW  = 20;
const REF_WIN_PCT   = 0.02;  // 2% of friend's win
const REF_DEP_PCT   = 0.05;  // 5% of friend's first deposit bonus

// ══════════════════ STATE ══════════════════
let state = {
  user: null, loggedIn: false,
  balance: 0, totalDeposited: 0, totalWon: 0, totalWithdrawn: 0,
  referrals: 0, refEarned: 0,
  bets: [{active:false,amount:0,cashedOut:false}, {active:false,amount:0,cashedOut:false}],
};
let gameState = {
  phase: 'waiting',
  multiplier: 1.00,
  crashAt: 1.00,
  history: [1.24, 3.56, 1.05, 847.32, 2.11, 1.43, 12.50, 1.02, 56.78, 1.89, 1203.45, 4.32, 1.01, 23.67, 1.76, 312.90, 1.34, 8.45, 1.08, 99.99],
  liveBets: [],
  roundInterval: null,
  flyInterval: null,
  countdown: 5,
};
let pendingSignup = null;
let pendingOTP    = null;

// ══════════════════ STORAGE (Supabase) ══════════════════
// Keep localStorage as fallback
const getUsers = () => JSON.parse(localStorage.getItem('av_users') || '{}');
const saveUsers = u => localStorage.setItem('av_users', JSON.stringify(u));

async function loadState() {
  const { data, error } = await sb.from('players').select('*').eq('email', state.user.email).single();
  if (data) {
    state.balance        = data.balance        || 0;
    state.totalDeposited = data.total_deposited || 0;
    state.totalWon       = data.total_won       || 0;
    state.totalWithdrawn = data.total_withdrawn || 0;
    state.referrals      = data.referrals       || 0;
    state.refEarned      = data.ref_earned      || 0;
  } else {
    // Fallback to localStorage
    const saved = JSON.parse(localStorage.getItem('av_' + state.user.email) || '{}');
    state.balance        = saved.balance        || 0;
    state.totalDeposited = saved.totalDeposited || 0;
    state.totalWon       = saved.totalWon       || 0;
    state.totalWithdrawn = saved.totalWithdrawn || 0;
    state.referrals      = saved.referrals      || 0;
    state.refEarned      = saved.refEarned      || 0;
  }
}

async function saveState() {
  if (!state.user) return;
  // Save to Supabase
  const { error } = await sb.from('players').upsert({
    email:            state.user.email,
    name:             state.user.name,
    phone:            state.user.phone || '',
    balance:          state.balance,
    total_deposited:  state.totalDeposited,
    total_won:        state.totalWon,
    total_withdrawn:  state.totalWithdrawn,
    referrals:        state.referrals,
    ref_earned:       state.refEarned,
    ref_code:         state.user.refCode || '',
    referred_by:      state.user.referredBy || '',
    updated_at:       new Date().toISOString()
  }, { onConflict: 'email' });
  // Also save to localStorage as backup
  localStorage.setItem('av_' + state.user.email, JSON.stringify({
    balance: state.balance, totalDeposited: state.totalDeposited,
    totalWon: state.totalWon, totalWithdrawn: state.totalWithdrawn,
    referrals: state.referrals, refEarned: state.refEarned,
  }));
}

async function saveNewUser(userData) {
  await sb.from('players').upsert({
    email:       userData.email,
    name:        userData.name,
    phone:       userData.phone || '',
    balance:     0,
    total_deposited: 0,
    total_won:   0,
    total_withdrawn: 0,
    referrals:   0,
    ref_earned:  0,
    ref_code:    userData.refCode || '',
    referred_by: userData.referredBy || '',
    created_at:  new Date().toISOString(),
    updated_at:  new Date().toISOString()
  }, { onConflict: 'email' });
}

// ══════════════════ UI HELPERS ══════════════════
function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}
function openModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }
function toast(msg, dur=3000) {
  const t = document.getElementById('toast');
  t.textContent = msg; t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), dur);
}
function fmt(n) { return parseFloat(n).toFixed(2); }
function updateBalDisplay() {
  document.getElementById('balDisplay').textContent = fmt(state.balance);
  document.getElementById('wBal').textContent       = fmt(state.balance);
  document.getElementById('wTotalDep').textContent  = fmt(state.totalDeposited);
  document.getElementById('wTotalWon').textContent  = fmt(state.totalWon);
  document.getElementById('wTotalWith').textContent = fmt(state.totalWithdrawn);
  document.getElementById('refCount').textContent   = state.referrals;
  document.getElementById('refEarned').textContent  = fmt(state.refEarned);
}

// ══════════════════ TELEGRAM NOTIFY ══════════════════
async function tgWelcome(telegramUsername, name) {
  if (!telegramUsername || telegramUsername.trim() === '') return;
  const username = telegramUsername.replace('@', '').trim();
  const msg = `🚀 Welcome to <b>AVIACOM</b>, ${name}!\n\nYour account is ready. Deposit GHS 5 or more to start playing.\n\nGood luck and ride the rocket! 🔥`;
  try {
    // First get chat id from username via getUpdates approach
    // We send via username directly
    await fetch(`https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage`, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ chat_id: '@' + username, text: msg, parse_mode: 'HTML' })
    });
  } catch(e) {}
}

async function tgNotify(msg) {
  if (!TG_BOT_TOKEN || TG_BOT_TOKEN.startsWith('YOUR')) return;
  try {
    await fetch(`https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage`, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ chat_id: TG_CHAT_ID, text: msg, parse_mode: 'HTML' })
    });
  } catch(e) {}
}

// ══════════════════ EMAILJS OTP ══════════════════
function generateOTP() { return Math.floor(100000 + Math.random() * 900000).toString(); }
async function sendOTP(email, name, code) {
  try {
    const result = await emailjs.send("service_pl4kshn", "template_74chryr", {
      email: email,
      to_name: name,
      otp_code: code
    });
    console.log('EmailJS success:', result);
    return true;
  } catch(e) {
    console.error('EmailJS error:', JSON.stringify(e));
    // Status 0 = CORS block (local file). Show code on screen for testing.
    if (e.status === 0) {
      // Running locally — show code in alert so it's impossible to miss
      setTimeout(() => alert(`TEST MODE\n\nYour verification code is:\n\n${code}\n\nThis will send to email when hosted on Netlify.`), 300);
      return true;
    }
    toast('Email error: ' + (e.text || e.message || JSON.stringify(e)));
    return false;
  }
}

// ══════════════════ GOOGLE SIGN IN ══════════════════
const GOOGLE_CLIENT_ID = "1069836497813-0hpniku55dagdv5jpotoku432fnn0dvp.apps.googleusercontent.com";

function googleSignIn() {
  if (GOOGLE_CLIENT_ID.startsWith('YOUR')) {
    toast('Google Sign-In not configured yet. Use email signup for now.'); return;
  }
  const client = google.accounts.oauth2.initTokenClient({
    client_id: GOOGLE_CLIENT_ID,
    scope: 'email profile',
    callback: (tokenResponse) => {
      if (tokenResponse.access_token) {
        fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
          headers: { Authorization: 'Bearer ' + tokenResponse.access_token }
        })
        .then(r => r.json())
        .then(payload => { handleGooglePayload(payload); });
      }
    },
  });
  client.requestAccessToken({ prompt: 'select_account' });
}

function handleGooglePayload(payload) { handleGoogleResponse({ _payload: payload }); }

function handleGoogleResponse(response) {
  try {
    let payload;
    if (response._payload) {
      payload = response._payload;
    } else {
      const base64 = response.credential.split('.')[1];
      payload = JSON.parse(atob(base64));
    }
    const { name, email, picture } = payload;

    const users = getUsers();
    if (users[email]) {
      // Existing user — log in
      state.user = users[email];
      state.loggedIn = true;
      loadState();
      closeModal('signupModal');
      closeModal('loginModal');
      enterGame();
      toast(`Welcome back, ${name.split(' ')[0]}! 🚀`);
    } else {
      // New user — auto create account
      const myRef = name.split(' ')[0].toUpperCase() + Math.random().toString(36).substr(2,5).toUpperCase();
      const ref   = document.getElementById('su-ref')?.value?.trim()?.toUpperCase() || '';
      users[email] = { name, email, phone: '', pass: '', refCode: myRef, referredBy: ref || null, verified: true, googleUser: true, picture };
      saveUsers(users);

      if (ref) {
        const referrer = Object.values(users).find(u => u.refCode === ref);
        if (referrer) {
          const rKey = 'av_' + referrer.email;
          const rData = JSON.parse(localStorage.getItem(rKey) || '{}');
          rData.referrals = (rData.referrals || 0) + 1;
          localStorage.setItem(rKey, JSON.stringify(rData));
        }
      }

      state.user = users[email];
      state.loggedIn = true;
      state.balance = 0; state.totalDeposited = 0; state.totalWon = 0;
      state.totalWithdrawn = 0; state.referrals = 0; state.refEarned = 0;
      saveState();
      closeModal('signupModal');
      closeModal('loginModal');
      enterGame();
      tgNotify(`🆕 <b>NEW SIGNUP (Google)</b>\nName: ${name}\nEmail: ${email}`);
      toast(`Welcome to Aviacom, ${name.split(' ')[0]}! 🚀`);
    }
  } catch(e) {
    toast('Google sign-in failed. Try email instead.'); console.error(e);
  }
}


async function doSignupStep1() {
  const name  = document.getElementById('su-name').value.trim();
  const email = document.getElementById('su-email').value.trim().toLowerCase();
  const phone = document.getElementById('su-phone').value.trim();
  const pass  = document.getElementById('su-pass').value;
  const ref   = document.getElementById('su-ref').value.trim().toUpperCase();
  const terms = document.getElementById('su-terms').checked;

  if (!name || !email || !phone || !pass) { toast('Fill all fields ❌'); return; }
  if (pass.length < 6) { toast('Password min 6 characters ❌'); return; }
  if (!terms) { toast('Accept Terms & Conditions ❌'); return; }
  if (!email.includes('@')) { toast('Invalid email ❌'); return; }

  const users = getUsers();
  if (users[email]) { toast('Email already registered ❌'); return; }

  const myRef = name.split(' ')[0].toUpperCase() + Math.random().toString(36).substr(2,5).toUpperCase();
  users[email] = { name, email, phone, pass, refCode: myRef, referredBy: ref || null, verified: true };
  saveUsers(users);

  if (ref) {
    const referrer = Object.values(users).find(u => u.refCode === ref);
    if (referrer) {
      const rKey = 'av_' + referrer.email;
      const rData = JSON.parse(localStorage.getItem(rKey) || '{}');
      rData.referrals = (rData.referrals || 0) + 1;
      localStorage.setItem(rKey, JSON.stringify(rData));
    }
  }

  state.user = users[email];
  state.loggedIn = true;
  state.balance = 0; state.totalDeposited = 0; state.totalWon = 0;
  state.totalWithdrawn = 0; state.referrals = 0; state.refEarned = 0;
  saveState();
  closeModal('signupModal');
  enterGame();
  const tgUser = document.getElementById('su-tg') ? document.getElementById('su-tg').value : '';
  tgNotify(`🆕 <b>NEW SIGNUP</b>\nName: ${name}\nEmail: ${email}\nPhone: ${phone}\nTelegram: ${tgUser || 'none'}\nRef: ${ref || 'none'}`);
  tgWelcome(tgUser, name.split(' ')[0]);
  toast('Welcome to Aviacom, ' + name.split(' ')[0] + '! 🚀');
}

function otpNext(idx) {
  const v = document.getElementById('otp'+idx).value;
  if (v && idx < 5) document.getElementById('otp'+(idx+1)).focus();
}

function getOTPValue() {
  return [0,1,2,3,4,5].map(i => document.getElementById('otp'+i).value).join('');
}

async function verifyOTP() {
  const entered = getOTPValue();
  // If EmailJS not configured, accept any 6-digit code for testing
  const valid = EMAILJS_KEY.startsWith('YOUR') ? entered.length === 6 : entered === pendingOTP;
  if (!valid) { toast('Wrong code ❌ Try again'); return; }

  const { name, email, phone, pass, ref } = pendingSignup;
  const users = getUsers();
  const myRef = name.split(' ')[0].toUpperCase() + Math.random().toString(36).substr(2,5).toUpperCase();
  users[email] = { name, email, phone, pass, refCode: myRef, referredBy: ref || null, verified: true };
  saveUsers(users);

  // Credit referrer first-deposit bonus setup flag
  if (ref) {
    const referrer = Object.values(users).find(u => u.refCode === ref);
    if (referrer) {
      const rKey = 'av_' + referrer.email;
      const rData = JSON.parse(localStorage.getItem(rKey) || '{}');
      rData.referrals = (rData.referrals || 0) + 1;
      localStorage.setItem(rKey, JSON.stringify(rData));
    }
  }

  state.user = users[email];
  state.loggedIn = true;
  state.balance = 0; state.totalDeposited = 0; state.totalWon = 0;
  state.totalWithdrawn = 0; state.referrals = 0; state.refEarned = 0;
  await saveState();
  await saveNewUser(users[email]);
  closeModal('signupModal');
  enterGame();
  tgNotify(`🆕 <b>NEW SIGNUP</b>\nName: ${name}\nEmail: ${email}\nPhone: ${phone}\nRef: ${ref || 'none'}\n\n📊 <b>AVIACOM DASHBOARD</b>`);
  toast(`Welcome to Aviacom, ${name.split(' ')[0]}! 🚀`);
}

async function resendOTP() {
  if (!pendingSignup) return;
  pendingOTP = generateOTP();
  await sendOTP(pendingSignup.email, pendingSignup.name, pendingOTP);
  toast('New code sent! 📧');
}

function doLogin() {
  const email = document.getElementById('li-email').value.trim().toLowerCase();
  const pass  = document.getElementById('li-pass').value;
  const users = getUsers();
  if (!users[email] || users[email].pass !== pass) { toast('Invalid email or password ❌'); return; }
  state.user = users[email];
  state.loggedIn = true;
  closeModal('loginModal');
  enterGame();
  toast(`Welcome back, ${state.user.name.split(' ')[0]}! 🚀`);
}

function doLogout() {
  saveState();
  state.loggedIn = false; state.user = null;
  showPage('landingPage');
  document.getElementById('heroBtns').style.display = 'flex';
  clearInterval(gameState.roundInterval);
  clearInterval(gameState.flyInterval);
}

async function enterGame() {
  document.getElementById('heroBtns').style.display = 'none';
  showPage('gamePage');
  await loadState();
  updateBalDisplay();
  const base = window.location.href.split('?')[0];
  document.getElementById('refLinkBox').textContent = base + '?ref=' + state.user.refCode;
  startGameLoop();
  buildTicker();
  buildFakeLiveBets();
  updateHistory();
}

// ══════════════════ DEPOSIT ══════════════════
function doDeposit() {
  const amt = parseFloat(document.getElementById('dep-amt').value);
  if (!amt || amt < 5) { toast('Minimum deposit is GHS 5 ❌'); return; }

  if (typeof PaystackPop === 'undefined') {
    const s = document.createElement('script');
    s.src = 'https://js.paystack.co/v1/inline.js';
    document.head.appendChild(s);
    toast('Loading payment... tap again ⏳'); return;
  }

  const ref = 'AV-DEP-' + state.user.email.replace(/[@.]/g,'_') + '-' + Date.now();
  const handler = PaystackPop.setup({
    key: PAYSTACK_KEY,
    email: state.user.email,
    amount: Math.round(amt * 100),
    currency: 'GHS',
    ref,
    callback: function(res) {
      // Credit referrer first deposit bonus
      const users = getUsers();
      const u = users[state.user.email];
      if (u.referredBy && !u.firstDepositDone) {
        const referrer = Object.values(users).find(r => r.refCode === u.referredBy);
        if (referrer) {
          const rKey = 'av_' + referrer.email;
          const rData = JSON.parse(localStorage.getItem(rKey) || '{}');
          const bonus = parseFloat((amt * REF_DEP_PCT).toFixed(2));
          rData.balance  = (rData.balance  || 0) + bonus;
          rData.refEarned = (rData.refEarned || 0) + bonus;
          localStorage.setItem(rKey, JSON.stringify(rData));
          tgNotify(`💎 <b>REFERRAL FIRST-DEPOSIT BONUS</b>\nReferrer: ${referrer.name}\nBonus: GHS ${bonus}\nNew player: ${state.user.name} deposited GHS ${amt}`);
        }
        u.firstDepositDone = true;
        saveUsers(users);
      }

      state.balance        += amt;
      state.totalDeposited += amt;
      saveState();
      updateBalDisplay();
      closeModal('depositModal');
      toast(`✅ GHS ${fmt(amt)} deposited! Balance: GHS ${fmt(state.balance)}`);
      tgNotify(`💰 <b>DEPOSIT</b>\nPlayer: ${state.user.name} (${state.user.email})\nAmount: GHS ${fmt(amt)}\nBalance: GHS ${fmt(state.balance)}\nRef: ${res.reference}`);
    },
    onClose: () => toast('Payment cancelled')
  });
  handler.openIframe();
}

// ══════════════════ WITHDRAW ══════════════════
function switchWith(idx) {
  document.querySelectorAll('.dw-tab').forEach((t,i) => t.classList.toggle('active', i===idx));
  document.getElementById('withMoMo').style.display = idx===0?'block':'none';
  document.getElementById('withBank').style.display  = idx===1?'block':'none';
}
async function doWithdraw() {
  const amt = parseFloat(document.getElementById('w-amt').value);
  if (!amt || amt < MIN_WITHDRAW) { toast(`Minimum withdrawal is GHS ${MIN_WITHDRAW} ❌`); return; }
  if (amt > state.balance) { toast('Insufficient balance ❌'); return; }

  const isMoMo = document.getElementById('withMoMo').style.display !== 'none';
  let details = '';
  if (isMoMo) {
    const net = document.getElementById('w-network').value;
    const ph  = document.getElementById('w-phone').value;
    if (!ph) { toast('Enter phone number ❌'); return; }
    details = `${net} — ${ph}`;
  } else {
    const bank = document.getElementById('w-bank').value;
    const acc  = document.getElementById('w-acc').value;
    const acn  = document.getElementById('w-accname').value;
    if (!bank || !acc || !acn) { toast('Fill all bank details ❌'); return; }
    details = `${bank} — ${acc} (${acn})`;
  }

  state.balance        -= amt;
  state.totalWithdrawn += amt;
  saveState();
  updateBalDisplay();
  closeModal('walletModal');
  toast(`✅ Withdrawal of GHS ${fmt(amt)} requested! 24–48hrs processing.`);
  tgNotify(`💸 <b>WITHDRAWAL REQUEST</b>\nPlayer: ${state.user.name} (${state.user.email})\nAmount: GHS ${fmt(amt)}\nMethod: ${details}\nRemaining Balance: GHS ${fmt(state.balance)}`);
}

// ══════════════════ BET CONTROLS ══════════════════
function switchBetTab(idx) {
  document.querySelectorAll('.tab').forEach((t,i) => t.classList.toggle('active', i===idx));
  document.getElementById('betPanel0').style.display = idx===0 ? 'block' : 'none';
}
function setBet(slot, val) {
  document.getElementById('betAmt'+slot).value = val;
  document.getElementById('betBtn'+slot).textContent = `BET GHS ${val}`;
}
function halveBet(slot) {
  const el = document.getElementById('betAmt'+slot);
  el.value = Math.max(MIN_BET, parseFloat(el.value||MIN_BET)/2).toFixed(0);
  document.getElementById('betBtn'+slot).textContent = `BET GHS ${el.value}`;
}
function doubleBet(slot) {
  const el = document.getElementById('betAmt'+slot);
  el.value = Math.min(MAX_BET, parseFloat(el.value||MIN_BET)*2).toFixed(0);
  document.getElementById('betBtn'+slot).textContent = `BET GHS ${el.value}`;
}
function toggleAuto(slot) {}

// ══════════════════ GAME ENGINE ══════════════════
function generateCrashPoint() {
  const hasBet = state.bets && state.bets.some(b => b.active);

  if (!hasBet) {
    // No bet placed — generate high multipliers to influence player
    const r = Math.random();
    if (r < 0.10) return +(50 + Math.random() * 200).toFixed(2);
    if (r < 0.30) return +(20 + Math.random() * 30).toFixed(2);
    if (r < 0.60) return +(8 + Math.random() * 12).toFixed(2);
    if (r < 0.85) return +(4 + Math.random() * 4).toFixed(2);
    return +(2 + Math.random() * 2).toFixed(2);
  } else {
    // Bet is active — apply house edge (heavy loss bias)
    const r = Math.random();
    if (r < 0.55) return +(1 + Math.random() * 0.95).toFixed(2);
    if (r < 0.80) return +(2 + Math.random() * 0.95).toFixed(2);
    if (r < 0.92) return +(3 + Math.random() * 1.95).toFixed(2);
    if (r < 0.97) return +(5 + Math.random() * 4.9).toFixed(2);
    return +(10 + Math.random() * 40).toFixed(2);
  }
}

function startGameLoop() {
  startCountdown();
}

function startCountdown() {
  gameState.phase      = 'waiting';
  gameState.multiplier = 1.00;
  gameState.crashAt    = generateCrashPoint();
  gameState.countdown  = 5;

  document.getElementById('multDisplay').className = 'mult waiting';
  document.getElementById('multDisplay').textContent = 'WAITING...';
  document.getElementById('statusDisplay').textContent = `NEXT ROUND IN ${gameState.countdown}s`;
  document.getElementById('crashLabel').style.display = 'none';

  // Reset bet buttons
  document.getElementById('betBtn0').disabled  = false;
  document.getElementById('betBtn0').textContent = `BET GHS ${document.getElementById('betAmt0').value || MIN_BET}`;
  document.getElementById('cashBtn0').style.display = 'none';

  state.bets = [
    {active:false, amount:0, cashedOut:false},
    {active:false, amount:0, cashedOut:false},
  ];

  drawCanvas('waiting', 1.00);

  const timer = setInterval(() => {
    gameState.countdown--;
    document.getElementById('statusDisplay').textContent = `NEXT ROUND IN ${gameState.countdown}s`;
    if (gameState.countdown <= 0) {
      clearInterval(timer);
      startFlight();
    }
  }, 1000);
}

function startFlight() {
  gameState.phase = 'flying';
  document.getElementById('multDisplay').className = 'mult flying';
  document.getElementById('statusDisplay').textContent = 'CASH OUT NOW!';

  // Lock bet buttons
  document.getElementById('betBtn0').disabled = true;
  if (state.bets[0].active) document.getElementById('cashBtn0').style.display = 'block';

  let speed = 0.015;
  gameState.flyInterval = setInterval(() => {
    gameState.multiplier = parseFloat((gameState.multiplier + speed).toFixed(2));
    speed += 0.0004; // accelerate
    document.getElementById('multDisplay').textContent = gameState.multiplier.toFixed(2) + 'x';
    drawCanvas('flying', gameState.multiplier);

    // Auto cashout check
    if (state.bets[0].active && !state.bets[0].cashedOut) {
      const autoOn  = document.getElementById('autoOn0').checked;
      const autoVal = parseFloat(document.getElementById('autoVal0').value);
      if (autoOn && gameState.multiplier >= autoVal) cashOut(0);
    }

    if (gameState.multiplier >= gameState.crashAt) {
      clearInterval(gameState.flyInterval);
      doCrash();
    }
  }, 100);
}

function doCrash() {
  gameState.phase = 'crashed';
  document.getElementById('multDisplay').className    = 'mult crashed';
  document.getElementById('multDisplay').textContent  = gameState.crashAt.toFixed(2) + 'x';
  document.getElementById('statusDisplay').textContent = '💥 CRASHED!';
  document.getElementById('crashLabel').style.display  = 'block';
  document.getElementById('cashBtn0').style.display    = 'none';

  // Lose bets that didn't cash out
  if (state.bets[0].active && !state.bets[0].cashedOut) {
    toast(`💥 Crashed at ${gameState.crashAt.toFixed(2)}x — You lost GHS ${fmt(state.bets[0].amount)}`);
    tgNotify(`💥 <b>CRASH BET LOST</b>\nPlayer: ${state.user.name}\nBet: GHS ${fmt(state.bets[0].amount)}\nCrashed at: ${gameState.crashAt.toFixed(2)}x`);
    state.bets[0].active = false;
    saveState();
    updateBalDisplay();
  }

  drawCanvas('crashed', gameState.crashAt);

  // Add to history
  gameState.history.unshift(gameState.crashAt);
  if (gameState.history.length > 20) gameState.history.pop();
  updateHistory();

  // Next round after 3s
  setTimeout(() => startCountdown(), 3000);
}

function placeBet(slot) {
  if (gameState.phase !== 'waiting') { toast('Wait for next round ⏳'); return; }
  const amt = parseFloat(document.getElementById('betAmt'+slot).value);
  if (!amt || amt < MIN_BET) { toast(`Min bet is GHS ${MIN_BET} ❌`); return; }
  if (amt > MAX_BET) { toast(`Max bet is GHS ${MAX_BET} ❌`); return; }
  if (amt > state.balance) { toast('Insufficient balance ❌ Please deposit'); openModal('depositModal'); return; }

  state.balance -= amt;
  state.bets[slot] = { active: true, amount: amt, cashedOut: false };
  // Regenerate crash point now that a bet is active (apply house edge)
  gameState.crashAt = generateCrashPoint();
  saveState();
  updateBalDisplay();
  document.getElementById('betBtn'+slot).textContent = `✅ BET GHS ${fmt(amt)} PLACED`;
  document.getElementById('betBtn'+slot).disabled    = true;
  toast(`Bet of GHS ${fmt(amt)} placed! 🚀`);
  tgNotify(`🎯 <b>BET PLACED</b>\nPlayer: ${state.user.name}\nAmount: GHS ${fmt(amt)}\nBalance: GHS ${fmt(state.balance)}`);
}

function cashOut(slot) {
  if (!state.bets[slot].active || state.bets[slot].cashedOut) return;
  if (gameState.phase !== 'flying') return;

  const bet  = state.bets[slot].amount;
  const mult = gameState.multiplier;
  const gross = parseFloat((bet * mult).toFixed(2));
  const profit = parseFloat((gross - bet).toFixed(2));

  state.bets[slot].cashedOut = true;
  state.bets[slot].active    = false;
  state.balance   += gross;
  state.totalWon  += profit;
  saveState();
  updateBalDisplay();
  document.getElementById('cashBtn'+slot).style.display = 'none';

  // Referral win commission
  const users = getUsers();
  const u = users[state.user.email];
  if (u.referredBy) {
    const referrer = Object.values(users).find(r => r.refCode === u.referredBy);
    if (referrer) {
      const commission = parseFloat((profit * REF_WIN_PCT).toFixed(2));
      if (commission > 0) {
        const rKey  = 'av_' + referrer.email;
        const rData = JSON.parse(localStorage.getItem(rKey) || '{}');
        rData.balance   = (rData.balance   || 0) + commission;
        rData.refEarned = (rData.refEarned || 0) + commission;
        localStorage.setItem(rKey, JSON.stringify(rData));
        tgNotify(`🤝 <b>REFERRAL COMMISSION</b>\nReferrer: ${referrer.name}\nCommission: GHS ${commission}\nFrom: ${state.user.name} won GHS ${profit} at ${mult}x`);
      }
    }
  }

  // Show win modal
  document.getElementById('winMultDisp').textContent = mult.toFixed(2) + 'x';
  document.getElementById('winAmtDisp').textContent  = 'GHS ' + fmt(gross);
  openModal('winModal');

  toast(`🎉 Cashed out at ${mult.toFixed(2)}x! Won GHS ${fmt(gross)}`);
  tgNotify(`✅ <b>CASHOUT</b>\nPlayer: ${state.user.name}\nBet: GHS ${fmt(bet)} → Won GHS ${fmt(gross)} at ${mult.toFixed(2)}x\nProfit: GHS ${fmt(profit)}\nBalance: GHS ${fmt(state.balance)}`);
}

// ══════════════════ CANVAS ══════════════════
function drawCanvas(phase, mult) {
  const canvas = document.getElementById('rocketCanvas');
  if (!canvas) return;
  const W = canvas.width = canvas.offsetWidth;
  const H = canvas.height = 400;
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, W, H);

  // Stars
  ctx.fillStyle = '#080808';
  ctx.fillRect(0, 0, W, H);
  for (let i = 0; i < 80; i++) {
    const sx = (i * 137.5) % W;
    const sy = (i * 97.3)  % H;
    const r  = Math.random() < 0.3 ? 1.5 : 0.8;
    ctx.beginPath(); ctx.arc(sx, sy, r, 0, Math.PI*2);
    ctx.fillStyle = `rgba(255,255,255,${0.3 + Math.random()*0.5})`;
    ctx.fill();
  }

  if (phase === 'waiting') {
    // Launch pad
    drawRocket(ctx, W*0.15, H*0.8, 0, 1);
    // Grid lines
    ctx.strokeStyle = 'rgba(255,102,0,0.08)';
    ctx.lineWidth = 1;
    for (let i=0; i<5; i++) {
      ctx.beginPath(); ctx.moveTo(0, H*0.2 + i*H*0.15); ctx.lineTo(W, H*0.2 + i*H*0.15); ctx.stroke();
    }
    return;
  }

  if (phase === 'crashed') {
    // Red flash overlay
    ctx.fillStyle = 'rgba(255,34,68,0.08)';
    ctx.fillRect(0, 0, W, H);
    // Explosion particles
    for (let i = 0; i < 20; i++) {
      const angle = (i / 20) * Math.PI * 2;
      const dist  = 30 + Math.random() * 50;
      const ex    = W*0.8 + Math.cos(angle)*dist;
      const ey    = H*0.25 + Math.sin(angle)*dist;
      ctx.beginPath(); ctx.arc(ex, ey, 2 + Math.random()*5, 0, Math.PI*2);
      ctx.fillStyle = `hsl(${20 + Math.random()*30}, 100%, 60%)`;
      ctx.fill();
    }
    return;
  }

  // FLYING
  const progress = Math.min((mult - 1) / 15, 0.85);
  const rx = W * 0.15 + progress * W * 0.65;
  const ry = H * 0.85 - progress * H * 0.7;

  // Trail
  const grad = ctx.createLinearGradient(W*0.15, H*0.85, rx, ry);
  grad.addColorStop(0, 'rgba(255,102,0,0)');
  grad.addColorStop(1, 'rgba(255,153,0,0.4)');
  ctx.beginPath();
  ctx.moveTo(W*0.15, H*0.85);
  ctx.lineTo(rx, ry);
  ctx.strokeStyle = grad;
  ctx.lineWidth = 3;
  ctx.stroke();

  // Flame particles along trail
  for (let i = 0; i < 8; i++) {
    const t2 = i / 8;
    const px = W*0.15 + t2*(rx - W*0.15);
    const py = H*0.85 + t2*(ry - H*0.85);
    ctx.beginPath();
    ctx.arc(px + (Math.random()-0.5)*8, py + (Math.random()-0.5)*8, 2+Math.random()*4, 0, Math.PI*2);
    ctx.fillStyle = `rgba(255,${100+Math.random()*100},0,${0.3-t2*0.3})`;
    ctx.fill();
  }

  // Rocket angle
  const angle = -Math.atan2(progress * H * 0.7, progress * W * 0.65 || 0.01);
  drawRocket(ctx, rx, ry, angle, 1);
}

function drawRocket(ctx, x, y, angle, scale) {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(angle - Math.PI/2);
  ctx.scale(scale, scale);

  // Body
  ctx.beginPath();
  ctx.moveTo(0, -28);
  ctx.lineTo(10, 10);
  ctx.lineTo(-10, 10);
  ctx.closePath();
  ctx.fillStyle = '#FF6600';
  ctx.fill();

  // Nose
  ctx.beginPath();
  ctx.moveTo(0, -38);
  ctx.lineTo(8, -22);
  ctx.lineTo(-8, -22);
  ctx.closePath();
  ctx.fillStyle = '#FF9900';
  ctx.fill();

  // Wings
  ctx.beginPath(); ctx.moveTo(10, 5); ctx.lineTo(20, 16); ctx.lineTo(10, 12); ctx.closePath();
  ctx.fillStyle = '#FF4400'; ctx.fill();
  ctx.beginPath(); ctx.moveTo(-10, 5); ctx.lineTo(-20, 16); ctx.lineTo(-10, 12); ctx.closePath();
  ctx.fillStyle = '#FF4400'; ctx.fill();

  // Exhaust flame
  ctx.beginPath();
  ctx.moveTo(-5, 12); ctx.lineTo(0, 24 + Math.random()*8); ctx.lineTo(5, 12);
  ctx.closePath();
  ctx.fillStyle = `rgba(255,200,50,0.9)`;
  ctx.fill();

  ctx.restore();
}

// ══════════════════ HISTORY ══════════════════
function updateHistory() {
  const el = document.getElementById('histList');
  el.innerHTML = gameState.history.map(v => {
    let cls, label;
    if (v >= 100)      { cls = 'high'; label = v.toFixed(2) + 'x 🔥'; }
    else if (v >= 10)  { cls = 'high'; label = v.toFixed(2) + 'x'; }
    else if (v >= 3)   { cls = 'mid';  label = v.toFixed(2) + 'x'; }
    else               { cls = 'low';  label = v.toFixed(2) + 'x'; }
    const extra = v >= 100 ? 'style="background:rgba(255,215,0,0.15);color:#FFD700;border-color:rgba(255,215,0,0.4);font-size:.8rem"' : '';
    return `<div class="hist-chip ${cls}" ${extra}>${label}</div>`;
  }).join('');
}

// ══════════════════ LIVE TICKER ══════════════════
function buildTicker() {
  const names = ['Kofi','Ama','Kwame','Abena','Yaw','Akua','Kweku','Adjoa','Kojo','Efua'];
  const items = Array.from({length:16}, () => {
    const n = names[Math.floor(Math.random()*names.length)];
    const m = (1.1 + Math.random()*8).toFixed(2);
    const a = (500 + Math.random()*15000).toFixed(2);
    return `<div class="ticker-item">${n} cashed out at <span>${m}x</span> — GHS ${a}</div>`;
  });
  // Duplicate for seamless loop
  document.getElementById('tickerInner').innerHTML = items.join('') + items.join('');
}

// ══════════════════ FAKE LIVE BETS ══════════════════
function buildFakeLiveBets() {
  const names = ['Kofi B.','Ama K.','Kwame A.','Abena O.','Yaw D.','Akua M.','Player***'];
  const list = document.getElementById('betsList');
  const count = 8 + Math.floor(Math.random()*12);
  document.getElementById('liveCount').textContent = count + (state.user ? 1 : 0);

  list.innerHTML = Array.from({length: count}, () => {
    const n = names[Math.floor(Math.random()*names.length)];
    const a = (200 + Math.random()*12000).toFixed(2);
    const phase = Math.random();
    let multHtml;
    if (phase < 0.3)      multHtml = `<span class="bet-mult live">flying</span>`;
    else if (phase < 0.6) multHtml = `<span class="bet-mult won">${(1.1+Math.random()*5).toFixed(2)}x ✓</span>`;
    else                  multHtml = `<span class="bet-mult lost">crashed</span>`;
    return `<div class="bet-item"><span class="bet-user">${n}</span><span class="bet-amount">GHS ${a}</span>${multHtml}</div>`;
  }).join('');

  // Add real player bet if active
  if (state.bets[0].active) {
    const item = document.createElement('div');
    item.className = 'bet-item fade-in';
    item.innerHTML = `<span class="bet-user" style="color:var(--orange)">YOU</span><span class="bet-amount">GHS ${fmt(state.bets[0].amount)}</span><span class="bet-mult live">live</span>`;
    list.prepend(item);
  }
}

// ══════════════════ REFERRAL ══════════════════
function copyRef() {
  const link = document.getElementById('refLinkBox').textContent;
  navigator.clipboard.writeText(link).then(() => toast('Link copied! 🔗'));
}
function shareWhatsApp() {
  const link = document.getElementById('refLinkBox').textContent;
  window.open(`https://wa.me/?text=Join me on Aviacom and win real GHS! 🚀 ${encodeURIComponent(link)}`);
}
function shareTelegram() {
  const link = document.getElementById('refLinkBox').textContent;
  window.open(`https://t.me/share/url?url=${encodeURIComponent(link)}&text=Join Aviacom — ride the rocket and win real GHS!`);
}

// ══════════════════ BET AMOUNT SYNC ══════════════════
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('betAmt0').addEventListener('input', function() {
    document.getElementById('betBtn0').textContent = `BET GHS ${this.value || MIN_BET}`;
  });

  // Check referral param
  const ref = new URLSearchParams(window.location.search).get('ref');
  if (ref) {
    document.getElementById('su-ref').value = ref;
    openModal('signupModal');
  }

  // Auto-login if session stored
  const saved = localStorage.getItem('av_session');
  if (saved) {
    const sess = JSON.parse(saved);
    const users = getUsers();
    if (users[sess.email]) {
      state.user = users[sess.email];
      state.loggedIn = true;
      loadState();
      enterGame();
    }
  }
});

// Save session on login
const _origEnter = enterGame;
</script>
</body>
</html>
