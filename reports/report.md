# Facebook Performance Analysis Report

**Generated at (UTC):** 2025-11-30T05:54:17.383898

**User query:** Analyze ROAS drop in last 7 days

## 1. ROAS & CTR Over Time
- Latest window: 2025-03-25 to 2025-03-31
- Previous window: 2025-03-18 to 2025-03-24

- ROAS change (%): -12.84
- CTR change (%): 18.35

### Window Metrics
- **latest_roas**: 5.4455
- **previous_roas**: 6.2475
- **latest_ctr**: 0.0129
- **previous_ctr**: 0.0109
- **latest_spend**: 22691.95
- **previous_spend**: 26488.92

## 2. Drivers Behind ROAS Change
### By Platform
- **Facebook** → ROAS: 6.2895, CTR: 0.0139, Spend: 11944.14
- **Instagram** → ROAS: 4.5077, CTR: 0.0119, Spend: 10747.81

### By Audience Type
- **Broad** → ROAS: 4.9594, CTR: 0.0113, Spend: 10514.29
- **Lookalike** → ROAS: 5.9629, CTR: 0.0163, Spend: 6826.06
- **Retargeting** → ROAS: 5.7408, CTR: 0.0126, Spend: 5351.6

### Audience Fatigue Signals
- No strong audience fatigue signals detected.

## 3. Validated Hypotheses
- **Hypothesis:** ROAS decreased in the latest period compared to the previous window.
  - Type: roas_drop_over_time
  - Confidence: 0.70
  - Evidence: ROAS changed by -12.84%.

- **Hypothesis:** Specific platforms (e.g., Facebook vs Instagram) are driving the ROAS change.
  - Type: platform_roas_shift
  - Confidence: 0.50
  - Evidence: Platform ROAS spread is small; no strong platform driver detected.

- **Hypothesis:** Certain audience segments have disproportionately lower ROAS.
  - Type: audience_roas_shift
  - Confidence: 0.80
  - Evidence: 1 audience types have ROAS < 80% of median (6.84).
  - Segments: [{'audience_type': 'Broad', 'roas': 5.079852886946433, 'spend': 221062.63999999998}]

- **Hypothesis:** No strong audience fatigue patterns are visible in the current horizon.
  - Type: audience_fatigue
  - Confidence: 0.40
  - Evidence: Fatigue check returned no strong downward CTR/ROAS trends.

- **Hypothesis:** Low-CTR creatives with high impressions are pulling down overall account performance.
  - Type: creative_underperformance
  - Confidence: 0.85
  - Evidence: Found 173 creative-audience-platform combinations with CTR < 0.01 and impressions >= 1000.
  - Segments: [{'creative_message': '3‑pack deal ends tonight — upgrade your men drawer with inner vests.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.006367964592831334, 'impressions': 871236, 'campaigns': ['Men_Premium_Modal', 'MEN_Signature_Soft']}, {'creative_message': '3‑pack deal ends tonight — upgrade your men drawer with inner vests.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.00947716182968674, 'impressions': 486116, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': '3‑pack deal ends tonight — upgrade your men drawer with trunks.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009326343147709389, 'impressions': 291647, 'campaigns': ['MEN Signature Soft', 'Men Bold Colors Drop']}, {'creative_message': '3‑pack deal ends tonight — upgrade your men drawer with trunks.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.004281450217684747, 'impressions': 262995, 'campaigns': ['Men_Bold_Colors_Drop']}, {'creative_message': '3‑pack deal ends tonight — upgrade your women drawer with boyshorts.', 'audience_type': 'Retargeting', 'platform': 'Facebook', 'ctr': 0.009302346372710733, 'impressions': 447414, 'campaigns': ['women | studio sports']}, {'creative_message': '3‑pack deal ends tonight — upgrade your women drawer with bras.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.0, 'impressions': 160268, 'campaigns': ['WOMEN_Seamless_Everyday']}, {'creative_message': '3‑pack deal ends tonight — upgrade your women drawer with panties.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.0, 'impressions': 168657, 'campaigns': ['Women_Fit_&_Lift']}, {'creative_message': '3‑pack deal ends tonight — upgrade your women drawer with panties.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.006734602949744668, 'impressions': 175066, 'campaigns': ['WOMEN  Seamless  Everyday']}, {'creative_message': '3‑pack deal ends tonight — upgrade your women drawer with sports bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009025966549357469, 'impressions': 199757, 'campaigns': ['Women | Studio Sports', 'Women | Studi Sports']}, {'creative_message': '3‑pack deal ends tonight — upgrade your women drawer with wire‑free bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008109849555173092, 'impressions': 934296, 'campaigns': ['WOMEN Seamless Everyday', 'Women_|_Studio_Sports', 'Women Cotton Classics']}, {'creative_message': 'All‑day comfort, zero pinch — try our men athletic briefs!', 'audience_type': 'Retargeting', 'platform': 'Facebook', 'ctr': 0.0, 'impressions': 273416, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'All‑day comfort, zero pinch — try our men boxers!', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008409352366446845, 'impressions': 123434, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'All‑day comfort, zero pinch — try our women boyshorts!', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.009171739826978532, 'impressions': 224712, 'campaigns': ['WOMEN C tton Classics']}, {'creative_message': 'All‑day comfort, zero pinch — try our women bras!', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008848315275061502, 'impressions': 420306, 'campaigns': ['women_Summer_Invisible']}, {'creative_message': 'All‑day comfort, zero pinch — try our women bras!', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009816781708735556, 'impressions': 471132, 'campaigns': ['Women | Studio Sports']}, {'creative_message': 'All‑day comfort, zero pinch — try our women panties!', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.0, 'impressions': 75692, 'campaigns': ['Women Summer Invisible']}, {'creative_message': 'All‑day comfort, zero pinch — try our women panties!', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.008770128162997043, 'impressions': 48688, 'campaigns': ['w men cotton classics']}, {'creative_message': 'All‑day comfort, zero pinch — try our women wire‑free bras!', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.00769786795005653, 'impressions': 971178, 'campaigns': ['Women | Studio Sports', 'WOMEN_Seamless_Everyday', 'WOMEN COTTON CLASSICS']}, {'creative_message': 'All‑day comfort, zero pinch — try our women wire‑free bras!', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.009662185063834596, 'impressions': 221275, 'campaigns': ['WOMEN SUMMER INVISIBLE']}, {'creative_message': 'All‑day comfort, zero pinch — try our women wire‑free bras!', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.008841598135482534, 'impressions': 511446, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Breathable bamboo that moves with you — limited offer on men athletic briefs.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.0039013732833957553, 'impressions': 83304, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Breathable bamboo that moves with you — limited offer on men briefs.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.0, 'impressions': 234013, 'campaigns': ['Men | Athleisure Cooling']}, {'creative_message': 'Breathable bamboo that moves with you — limited offer on men inner vests.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.0, 'impressions': 231495, 'campaigns': ['Men ComfortMax Launch']}, {'creative_message': 'Breathable bamboo that moves with you — limited offer on men inner vests.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007163942999649907, 'impressions': 462734, 'campaigns': ['Men  Premium  Modal']}, {'creative_message': 'Breathable bamboo that moves with you — limited offer on women bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009683965014577259, 'impressions': 214375, 'campaigns': ['women  Summer  Invisible']}, {'creative_message': 'Breathable bamboo that moves with you — limited offer on women bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.008131575007825366, 'impressions': 293916, 'campaigns': ['WOMEN  Seamless  Everyday', 'Women | Studio Sports']}, {'creative_message': 'Breathable bamboo that moves with you — limited offer on women panties.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.005825149853335034, 'impressions': 313640, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Breathable cotton that moves with you — limited offer on men athletic briefs.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.0060809102796563356, 'impressions': 640858, 'campaigns': ['MEN SIGNATURE SOFT', 'MEN PREMIUM MODAL']}, {'creative_message': 'Breathable cotton that moves with you — limited offer on women sports bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.005056368121613034, 'impressions': 399694, 'campaigns': ['WOMEN Cotton Classics']}, {'creative_message': 'Breathable microfiber that moves with you — limited offer on men inner vests.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008813496273814406, 'impressions': 709707, 'campaigns': ['Men  Premium  Modal', 'men comfortmax launch']}, {'creative_message': 'Breathable microfiber that moves with you — limited offer on women boyshorts.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.009221101523189362, 'impressions': 307447, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Breathable microfiber that moves with you — limited offer on women bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008357444794613374, 'impressions': 92971, 'campaigns': ['WOMEN  Cotton  Classics']}, {'creative_message': 'Breathable microfiber that moves with you — limited offer on women sports bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.005438850577767148, 'impressions': 225783, 'campaigns': ['WOEN  Cotton  Classics']}, {'creative_message': 'Breathable microfiber that moves with you — limited offer on women wire‑free bras.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.008988865144528175, 'impressions': 444550, 'campaigns': ['Women-Studio Sports']}, {'creative_message': 'Breathable modal that moves with you — limited offer on men briefs.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.009262282251392025, 'impressions': 223595, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Breathable organic cotton that moves with you — limited offer on women sports bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.00631377634560721, 'impressions': 76341, 'campaigns': ['WOMEN_Seamless_Everyday']}, {'creative_message': 'Confidence starts inside — elevate with men boxers.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.004642673932713451, 'impressions': 387923, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Confidence starts inside — elevate with men trunks.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.007913089022509258, 'impressions': 969912, 'campaigns': ['Men | Athleisure Cooling', 'Men-Athleisure Cooling']}, {'creative_message': 'Confidence starts inside — elevate with men trunks.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.00867054370603811, 'impressions': 492472, 'campaigns': ['Men_Premium_Modal']}, {'creative_message': 'Confidence starts inside — elevate with women boyshorts.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.007800409560582139, 'impressions': 319855, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Confidence starts inside — elevate with women boyshorts.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.009220372020851634, 'impressions': 467877, 'campaigns': ['WOMEN SEAMLESS EVERYDAY']}, {'creative_message': 'Confidence starts inside — elevate with women boyshorts.', 'audience_type': 'Retargeting', 'platform': 'Facebook', 'ctr': 0.0, 'impressions': 239668, 'campaigns': ['women | studio sports']}, {'creative_message': 'Confidence starts inside — elevate with women bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008523919429290809, 'impressions': 114384, 'campaigns': ['WOMEN Cotton Classics', 'Women Cotton Classics']}, {'creative_message': 'Confidence starts inside — elevate with women panties.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008160977466034496, 'impressions': 388924, 'campaigns': ['WOMEN_Seamless_Everyday']}, {'creative_message': 'Confidence starts inside — elevate with women panties.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.004956727948366908, 'impressions': 163616, 'campaigns': ['WOMEN_Cotton_Classics']}, {'creative_message': 'Confidence starts inside — elevate with women sports bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.00992854951124359, 'impressions': 684390, 'campaigns': ['women_Summer_Invisible', 'WOMEN_Seamless_Everyday', 'women Summer Invisible']}, {'creative_message': 'Confidence starts inside — elevate with women wire‑free bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009851892278450044, 'impressions': 106274, 'campaigns': ['WOMEN SUMMER INVISIBLE']}, {'creative_message': 'Confidence starts inside — elevate with women wire‑free bras.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.00894467052862383, 'impressions': 338861, 'campaigns': ['women seamless-everyday']}, {'creative_message': 'Confidence starts inside — elevate with women wire‑free bras.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.00974332560734827, 'impressions': 69894, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Cooling mesh panels for workouts — men briefs you’ll actually love.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009719375865877561, 'impressions': 1253064, 'campaigns': ['Men Bold Colors Drop', 'MEN  Signature  Soft']}, {'creative_message': 'Cooling mesh panels for workouts — men briefs you’ll actually love.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.007275309445146038, 'impressions': 235179, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Cooling mesh panels for workouts — men inner vests you’ll actually love.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008776282329591267, 'impressions': 451444, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'Cooling mesh panels for workouts — women boyshorts you’ll actually love.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.009461326332392935, 'impressions': 377854, 'campaigns': ['WOMEN COTTON CLASSICS']}, {'creative_message': 'Cooling mesh panels for workouts — women bras you’ll actually love.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.009803355857565865, 'impressions': 329275, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Cooling mesh panels for workouts — women panties you’ll actually love.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009682663518762841, 'impressions': 489638, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Cooling mesh panels for workouts — women panties you’ll actually love.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008865107885196852, 'impressions': 189507, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Cooling mesh panels for workouts — women panties you’ll actually love.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.007027146451148504, 'impressions': 140313, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Doctors recommend breathable bamboo — meet our men trunks.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009573673302164168, 'impressions': 331952, 'campaigns': ['MEN PREMIUM MODAL']}, {'creative_message': 'Doctors recommend breathable bamboo — meet our women panties.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008136835271722985, 'impressions': 363532, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Doctors recommend breathable bamboo — meet our women wire‑free bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009742635529259268, 'impressions': 47831, 'campaigns': ['women summer invisible']}, {'creative_message': 'Doctors recommend breathable cotton — meet our men briefs.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.008008292547393618, 'impressions': 467890, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Doctors recommend breathable cotton — meet our women boyshorts.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008609561269753258, 'impressions': 461696, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Doctors recommend breathable cotton — meet our women boyshorts.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.007790195432799396, 'impressions': 258145, 'campaigns': ['women fit & li t']}, {'creative_message': 'Doctors recommend breathable microfiber — meet our men athletic briefs.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008003401179784238, 'impressions': 470425, 'campaigns': ['MEN BOLD COLORS DROP']}, {'creative_message': 'Doctors recommend breathable microfiber — meet our men briefs.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.006079735206968655, 'impressions': 403636, 'campaigns': ['Me   Premium  Modal']}, {'creative_message': 'Doctors recommend breathable microfiber — meet our women bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.00891156462585034, 'impressions': 147000, 'campaigns': ['Women | Studio Sports']}, {'creative_message': 'Doctors recommend breathable microfiber — meet our women panties.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007369822473012353, 'impressions': 242611, 'campaigns': ['WOMEN_Seamless_Everyday']}, {'creative_message': 'Doctors recommend breathable microfiber — meet our women panties.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.008976335829819371, 'impressions': 381336, 'campaigns': ['women | studio sports']}, {'creative_message': 'Doctors recommend breathable microfiber — meet our women sports bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.0074188738518274015, 'impressions': 439285, 'campaigns': ['WOMEN Seamless Everyday', 'WOMEN_Seamless_Everyday']}, {'creative_message': 'Doctors recommend breathable microfiber — meet our women sports bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.005684334858998967, 'impressions': 81276, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Doctors recommend breathable modal — meet our men athletic briefs.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.005947493751151403, 'impressions': 439681, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Doctors recommend breathable modal — meet our men boxers.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.005063246968507372, 'impressions': 286575, 'campaigns': ['Men_Bold_Colors_Drop']}, {'creative_message': 'Doctors recommend breathable modal — meet our men briefs.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008178496728357246, 'impressions': 409733, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'Doctors recommend breathable modal — meet our men briefs.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.006844806496765488, 'impressions': 396505, 'campaigns': ['men bold colors drop']}, {'creative_message': 'Doctors recommend breathable modal — meet our women sports bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009591860629926112, 'impressions': 324546, 'campaigns': ['WOMEN Cotton Classics']}, {'creative_message': 'Doctors recommend breathable modal — meet our women wire‑free bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009101419733806761, 'impressions': 182499, 'campaigns': ['WOMEN COTTON CLASSICS']}, {'creative_message': 'Doctors recommend breathable organic cotton — meet our men trunks.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008735755594055782, 'impressions': 163924, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'Doctors recommend breathable organic cotton — meet our women boyshorts.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007487603209472255, 'impressions': 343234, 'campaigns': ['WOMEN  Cotton  Classics']}, {'creative_message': 'Doctors recommend breathable organic cotton — meet our women panties.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.00946618924147014, 'impressions': 48594, 'campaigns': ['Women Fit & Lift']}, {'creative_message': 'Doctors recommend breathable organic cotton — meet our women sports bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.006757025793761398, 'impressions': 251146, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Doctors recommend breathable organic cotton — meet our women wire‑free bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.005869762913019116, 'impressions': 108863, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Hot & comfy: men athletic briefs now 20% off — feel the difference.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.00480708109392878, 'impressions': 542741, 'campaigns': ['Men | Athleisure Cooling', 'Men Bold Colors Drop']}, {'creative_message': 'Hot & comfy: men boxers now 20% off — feel the difference.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.003904770448338417, 'impressions': 401304, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Hot & comfy: men boxers now 20% off — feel the difference.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.0, 'impressions': 52070, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'Hot & comfy: men briefs now 20% off — feel the difference.', 'audience_type': 'Retargeting', 'platform': 'Facebook', 'ctr': 0.008683963613859738, 'impressions': 150277, 'campaigns': ['men bld colors drop']}, {'creative_message': 'Hot & comfy: men inner vests now 20% off — feel the difference.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.0, 'impressions': 251310, 'campaigns': ['Men | Athleisure Cooling']}, {'creative_message': 'Hot & comfy: men trunks now 20% off — feel the difference.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.005889600048078368, 'impressions': 99837, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'Hot & comfy: women bras now 20% off — feel the difference.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.0056314852243953386, 'impressions': 266182, 'campaigns': ['WOMEN  Seamless  Everyday']}, {'creative_message': 'Hot & comfy: women bras now 20% off — feel the difference.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.0033415747749013895, 'impressions': 540763, 'campaigns': ['WOMEN Cotton Classics', 'WOMEN COTTON CLASSICS']}, {'creative_message': 'Hot & comfy: women panties now 20% off — feel the difference.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.008221173043948041, 'impressions': 42573, 'campaigns': ['women cotton classics']}, {'creative_message': 'Hot & comfy: women sports bras now 20% off — feel the difference.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.0099504866726014, 'impressions': 271846, 'campaigns': ['women Summer Invisible']}, {'creative_message': 'Hot & comfy: women sports bras now 20% off — feel the difference.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.006983281890052897, 'impressions': 435755, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Hot & comfy: women wire‑free bras now 20% off — feel the difference.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009139330452414593, 'impressions': 169159, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Hot & comfy: women wire‑free bras now 20% off — feel the difference.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.006058958812460799, 'impressions': 478300, 'campaigns': ['WOMEN  Seamless  Everyday']}, {'creative_message': 'Hot & comfy: women wire‑free bras now 20% off — feel the difference.', 'audience_type': 'Retargeting', 'platform': 'Facebook', 'ctr': 0.007833052642373424, 'impressions': 253541, 'campaigns': ['WOMEN SEAMLESS EVERYDAY']}, {'creative_message': 'Invisible under tees — seamless men briefs.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009747496786215518, 'impressions': 508746, 'campaigns': ['MEN COMFORTMA LAUNCH', 'Men Bold Colors Drop']}, {'creative_message': 'Invisible under tees — seamless men trunks.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.0074502312068958345, 'impressions': 480522, 'campaigns': ['Men ComfortMax Launch', 'Men Bold Colors Drop']}, {'creative_message': 'Invisible under tees — seamless women boyshorts.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008000275871581778, 'impressions': 202993, 'campaigns': ['WOMEN_Seamless_Everyday']}, {'creative_message': 'Invisible under tees — seamless women boyshorts.', 'audience_type': 'Retargeting', 'platform': 'Facebook', 'ctr': 0.005194050355340678, 'impressions': 378510, 'campaigns': ['Women Summer Invisible']}, {'creative_message': 'Invisible under tees — seamless women bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008815197539379899, 'impressions': 461022, 'campaigns': ['women_Summer_Invisible']}, {'creative_message': 'Invisible under tees — seamless women bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.00906591938634353, 'impressions': 336866, 'campaigns': ['Women Cotton Classics']}, {'creative_message': 'Invisible under tees — seamless women sports bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008593108861903686, 'impressions': 168158, 'campaigns': ['women | studio sports']}, {'creative_message': 'Invisible under tees — seamless women wire‑free bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.008245473366762006, 'impressions': 83561, 'campaigns': ['women seamless everyday']}, {'creative_message': 'No ride‑up guarantee — best‑selling men boxers back in stock.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.00903761654019222, 'impressions': 472691, 'campaigns': ['Men | Athleisure Cooling']}, {'creative_message': 'No ride‑up guarantee — best‑selling men inner vests back in stock.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009420416739625284, 'impressions': 57110, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'No ride‑up guarantee — best‑selling women bras back in stock.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.005184277500235649, 'impressions': 159135, 'campaigns': ['Women Cotton Classics']}, {'creative_message': 'No ride‑up guarantee — best‑selling women panties back in stock.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008784796276768654, 'impressions': 252254, 'campaigns': ['WOMEN | STUDIO SPORTS', 'WOMEN  Seamles   Everyday']}, {'creative_message': 'No ride‑up guarantee — best‑selling women panties back in stock.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009863726347774044, 'impressions': 173768, 'campaigns': ['women | studio sports']}, {'creative_message': 'No ride‑up guarantee — best‑selling women panties back in stock.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.009248407643312102, 'impressions': 78500, 'campaigns': ['women | studio sports']}, {'creative_message': 'No ride‑up guarantee — best‑selling women sports bras back in stock.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.009157961603613778, 'impressions': 453376, 'campaigns': ['WOMEN Seamless Everyday', 'women Summer Invisible']}, {'creative_message': 'No ride‑up guarantee — best‑selling women sports bras back in stock.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.007725050889517863, 'impressions': 905884, 'campaigns': ['Women | Studio Sports', 'WOMEN Cotton Classics']}, {'creative_message': 'No ride‑up guarantee — best‑selling women wire‑free bras back in stock.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009821292337585906, 'impressions': 321139, 'campaigns': ['Women_|_Studio_Sports']}, {'creative_message': 'No ride‑up guarantee — best‑selling women wire‑free bras back in stock.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.009751585055150391, 'impressions': 325383, 'campaigns': ['women seamless everyday', 'women  Summer  Invisible']}, {'creative_message': 'No ride‑up guarantee — best‑selling women wire‑free bras back in stock.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.008090775467405652, 'impressions': 534065, 'campaigns': ['women  Summer  Invisible', 'WOMEN  Seamless- Everyday']}, {'creative_message': 'No ride‑up guarantee — best‑selling women wire‑free bras back in stock.', 'audience_type': 'Retargeting', 'platform': 'Facebook', 'ctr': 0.009660064903561071, 'impressions': 185506, 'campaigns': ['women  Summer  Invisible']}, {'creative_message': 'No ride‑up guarantee — best‑selling women wire‑free bras back in stock.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.008610241922883649, 'impressions': 236811, 'campaigns': ['WOMEN Cotton Classics', 'women cotton classics']}, {'creative_message': 'Push comfort, not wires — everyday men briefs.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007294779131144595, 'impressions': 328317, 'campaigns': ['men bold colors drop']}, {'creative_message': 'Push comfort, not wires — everyday men inner vests.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.006587214889405426, 'impressions': 243502, 'campaigns': ['MEN Signature Soft']}, {'creative_message': 'Push comfort, not wires — everyday men inner vests.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.0, 'impressions': 398592, 'campaigns': ['Men Comfortmax Launch']}, {'creative_message': 'Push comfort, not wires — everyday men inner vests.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.008678430455651982, 'impressions': 72709, 'campaigns': ['Men_Premium_Modal']}, {'creative_message': 'Push comfort, not wires — everyday women bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007601266035893464, 'impressions': 118796, 'campaigns': ['Women | Studio Sports']}, {'creative_message': 'Push comfort, not wires — everyday women panties.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.007937284079728093, 'impressions': 501053, 'campaigns': ['WOMEN  Seamless  Everyday', 'Women | Studio Sports']}, {'creative_message': 'Push comfort, not wires — everyday women sports bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.006878890222457923, 'impressions': 716540, 'campaigns': ['WOMEN SUMMER INVISIBLE', 'women Summer Invisible']}, {'creative_message': 'Push comfort, not wires — everyday women wire‑free bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.00956020961414299, 'impressions': 385661, 'campaigns': ['women cotton classics']}, {'creative_message': 'Push comfort, not wires — everyday women wire‑free bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.00891698981982655, 'impressions': 147247, 'campaigns': ['Women | Studio Sports']}, {'creative_message': 'Seamless confidence for every day — new men athletic briefs.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.005587274534867207, 'impressions': 352050, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Seamless confidence for every day — new men athletic briefs.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008043546936890963, 'impressions': 658416, 'campaigns': ['Men ComfortMax Launch', 'Men Bold Colors Drop']}, {'creative_message': 'Seamless confidence for every day — new men athletic briefs.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.009797813898170697, 'impressions': 17657, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Seamless confidence for every day — new men boxers.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.00913198832068265, 'impressions': 348993, 'campaigns': ['Men ComfortMax Launch', 'Men Premium Modal']}, {'creative_message': 'Seamless confidence for every day — new women boyshorts.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.006647664410148705, 'impressions': 213308, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Seamless confidence for every day — new women bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008251677610217188, 'impressions': 692950, 'campaigns': ['women cotton classics', 'women Summer Invisible']}, {'creative_message': 'Seamless confidence for every day — new women bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009415087678004001, 'impressions': 25491, 'campaigns': ['Women_|_Studio_Sports']}, {'creative_message': 'Seamless confidence for every day — new women bras.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.008552166042257251, 'impressions': 460702, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Seamless confidence for every day — new women bras.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.008527831826687645, 'impressions': 107413, 'campaigns': ['Women_|_Studio_Sports']}, {'creative_message': 'Seamless confidence for every day — new women wire‑free bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009355633118815914, 'impressions': 797915, 'campaigns': ['Women | Studio Sports', 'WOMEN SEAMLESS EVERYDAY', 'women Summer Invisible']}, {'creative_message': 'Seamless confidence for every day — new women wire‑free bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007290250630204965, 'impressions': 606152, 'campaigns': ['Women Seamless Everyday', 'women Summer Invisible']}, {'creative_message': 'Seamless confidence for every day — new women wire‑free bras.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.009947025420176074, 'impressions': 393585, 'campaigns': ['Women_|_Studio_Sports']}, {'creative_message': 'Seamless confidence for every day — new women wire‑free bras.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.009019999804019558, 'impressions': 204102, 'campaigns': ['Women Summer Invisible']}, {'creative_message': 'Stretch that snaps back — durable men athletic briefs.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.007655038515043716, 'impressions': 396079, 'campaigns': ['Men  Bold  Colors  Drop']}, {'creative_message': 'Stretch that snaps back — durable men boxers.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.009647880411156764, 'impressions': 71311, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Stretch that snaps back — durable men briefs.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.009388269208294919, 'impressions': 154022, 'campaigns': ['MEN Signature Soft']}, {'creative_message': 'Stretch that snaps back — durable men trunks.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007559417119826634, 'impressions': 197502, 'campaigns': ['MEN Signature Soft']}, {'creative_message': 'Stretch that snaps back — durable women boyshorts.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008258319509033387, 'impressions': 220626, 'campaigns': ['WOMEN_Seamless_Everyday']}, {'creative_message': 'Stretch that snaps back — durable women bras.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.0, 'impressions': 506661, 'campaigns': ['Women Seamless Everyday']}, {'creative_message': 'Stretch that snaps back — durable women sports bras.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009660105149817117, 'impressions': 491299, 'campaigns': ['WOMEN COTTON CLASSICS']}, {'creative_message': 'Stretch that snaps back — durable women sports bras.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.0093761891790168, 'impressions': 480899, 'campaigns': ['Women-Studio Sports']}, {'creative_message': 'Stretch that snaps back — durable women sports bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.007341206511330993, 'impressions': 25064, 'campaigns': ['Women  |  Studio  Sports']}, {'creative_message': 'Stretch that snaps back — durable women wire‑free bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008734700276598843, 'impressions': 89299, 'campaigns': ['Women_|_Studio_Sports', 'Women  Fit  &  Lift']}, {'creative_message': 'Stretch that snaps back — durable women wire‑free bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.0087214874448917, 'impressions': 41736, 'campaigns': ['WOMEN_Seamless_Everyday']}, {'creative_message': 'Summer‑ready essentials — sweat‑wicking men athletic briefs.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.008000149885712144, 'impressions': 213496, 'campaigns': ['Men Bold Colors Drop']}, {'creative_message': 'Summer‑ready essentials — sweat‑wicking men boxers.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.008039674501449377, 'impressions': 429495, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'Summer‑ready essentials — sweat‑wicking men briefs.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.007463856088830753, 'impressions': 478573, 'campaigns': ['MEN  Signature  Soft']}, {'creative_message': 'Summer‑ready essentials — sweat‑wicking women bras.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.00953144486014609, 'impressions': 44904, 'campaigns': ['WOMEN SUMMER INVISIBLE']}, {'creative_message': 'Summer‑ready essentials — sweat‑wicking women panties.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.009739124378427085, 'impressions': 689179, 'campaigns': ['WOMEN  Cotton  Classics', 'WOMEN  Seamless  Everyday', 'WOMEN Cotton Classics', 'women s-mmer invisible']}, {'creative_message': 'Summer‑ready essentials — sweat‑wicking women panties.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007427259186936791, 'impressions': 200747, 'campaigns': ['WOMEN Cotton Classics']}, {'creative_message': 'Summer‑ready essentials — sweat‑wicking women sports bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.0059305667492890925, 'impressions': 65761, 'campaigns': ['WOMEN_Cotton_Classics']}, {'creative_message': 'Summer‑ready essentials — sweat‑wicking women sports bras.', 'audience_type': 'Lookalike', 'platform': 'Instagram', 'ctr': 0.009394601651860473, 'impressions': 352330, 'campaigns': ['women  Summer  Invi ible']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium men boxers.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.0, 'impressions': 178715, 'campaigns': ['men comfortmax launch']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium men briefs.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.0042583412478546245, 'impressions': 354833, 'campaigns': ['MEN BOLD COLORS DROP']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium men briefs.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.008195222906296151, 'impressions': 902599, 'campaigns': ['Men Bold Colors Drop', 'men bold colors drop']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium women boyshorts.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008786106224644003, 'impressions': 209763, 'campaigns': ['WOMEN Seamless Everyday', 'Women Summer Invisible']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium women bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008936708089387393, 'impressions': 1083061, 'campaigns': ['women seamless everyday', 'WOMEN_Seamless_Everyday', 'Women Seamless Everyday', 'women Summer Invisible']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium women panties.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.0075578960558466525, 'impressions': 303259, 'campaigns': ['Women | Studio Sports']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium women sports bras.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.007728798027033947, 'impressions': 296812, 'campaigns': ['women_Summer_Invisible', 'WOMEN Cotton Classics']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium women sports bras.', 'audience_type': 'Lookalike', 'platform': 'Facebook', 'ctr': 0.009795533684700465, 'impressions': 517787, 'campaigns': ['WOMEN Seamless Everyday']}, {'creative_message': 'Ultra‑soft waistband, no marks — premium women sports bras.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.008650929460922155, 'impressions': 316151, 'campaigns': ['women summer invisible']}, {'creative_message': 'Wire‑free ease, cloud‑soft cups — men athletic briefs that fits right.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.006041097598295345, 'impressions': 352916, 'campaigns': ['MEN BOLD COLORS DROP', 'Men  Bold  Colors  Drop']}, {'creative_message': 'Wire‑free ease, cloud‑soft cups — men boxers that fits right.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.008462210027438265, 'impressions': 160360, 'campaigns': ['Men Premium Modal']}, {'creative_message': 'Wire‑free ease, cloud‑soft cups — men trunks that fits right.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.008900345560736994, 'impressions': 788284, 'campaigns': ['Men ComfortMax Launch', 'Men Bold Colors Drop', 'Men_|_Athleisure_Cooling']}, {'creative_message': 'Wire‑free ease, cloud‑soft cups — women panties that fits right.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.002754865887254462, 'impressions': 735426, 'campaigns': ['WOMEN Seamless Everyday', 'WOMEN SEAMLESS EVERYDAY']}, {'creative_message': 'Wire‑free ease, cloud‑soft cups — women panties that fits right.', 'audience_type': 'Broad', 'platform': 'Instagram', 'ctr': 0.00994920975881416, 'impressions': 1106118, 'campaigns': ['WOMEN_Cotton_Classics', 'WOMEN Cotton Classics', 'WOMEN SEAMLESS EVERYDAY', 'Women  Fit  &  Lift']}, {'creative_message': 'Wire‑free ease, cloud‑soft cups — women wire‑free bras that fits right.', 'audience_type': 'Broad', 'platform': 'Facebook', 'ctr': 0.008552203111857596, 'impressions': 758518, 'campaigns': ['Women Fit & Lift', 'women summer invisible']}, {'creative_message': 'Wire‑free ease, cloud‑soft cups — women wire‑free bras that fits right.', 'audience_type': 'Retargeting', 'platform': 'Instagram', 'ctr': 0.007916687301463773, 'impressions': 424041, 'campaigns': ['WOMEN Seamless Everyday']}]

## 4. Creative Recommendations for Low-CTR Campaigns
- **Campaign:** Men_Premium_Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: 3‑pack deal ends tonight — upgrade your men drawer with inner vests.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your men drawer with inner vests. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: 3‑pack deal ends tonight — upgrade your men drawer with inner vests.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your men drawer with inner vests. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching,...
  - CTA suggestion: Shop Now

- **Campaign:** MEN Signature Soft
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: 3‑pack deal ends tonight — upgrade your men drawer with trunks.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your men drawer with trunks. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** Men_Bold_Colors_Drop
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: 3‑pack deal ends tonight — upgrade your men drawer with trunks.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your men drawer with trunks. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging...
  - CTA suggestion: Try It Today

- **Campaign:** women | studio sports
  - Audience Type: Retargeting
  - Platform: Facebook
  - Old message: 3‑pack deal ends tonight — upgrade your women drawer with boyshorts.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your women drawer with boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN_Seamless_Everyday
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: 3‑pack deal ends tonight — upgrade your women drawer with bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your women drawer with bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Women_Fit_&_Lift
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: 3‑pack deal ends tonight — upgrade your women drawer with panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your women drawer with panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** WOMEN  Seamless  Everyday
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: 3‑pack deal ends tonight — upgrade your women drawer with panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your women drawer with panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging...
  - CTA suggestion: Explore Collection

- **Campaign:** Women | Studio Sports
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: 3‑pack deal ends tonight — upgrade your women drawer with sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: 3‑pack deal ends tonight — upgrade your women drawer with sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: 3‑pack deal ends tonight — upgrade your women drawer with wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: 3‑pack deal ends tonight — upgrade your women drawer with wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Retargeting
  - Platform: Facebook
  - Old message: All‑day comfort, zero pinch — try our men athletic briefs!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our men athletic briefs! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** Men Premium Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: All‑day comfort, zero pinch — try our men boxers!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our men boxers! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN C tton Classics
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: All‑day comfort, zero pinch — try our women boyshorts!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our women boyshorts! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Explore Collection

- **Campaign:** women_Summer_Invisible
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: All‑day comfort, zero pinch — try our women bras!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our women bras! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Try It Today

- **Campaign:** Women | Studio Sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: All‑day comfort, zero pinch — try our women bras!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our women bras! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Women Summer Invisible
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: All‑day comfort, zero pinch — try our women panties!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our women panties! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** w men cotton classics
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: All‑day comfort, zero pinch — try our women panties!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our women panties! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** Women | Studio Sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: All‑day comfort, zero pinch — try our women wire‑free bras!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our women wire‑free bras! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** WOMEN SUMMER INVISIBLE
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: All‑day comfort, zero pinch — try our women wire‑free bras!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our women wire‑free bras! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Try It Today

- **Campaign:** women Summer Invisible
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: All‑day comfort, zero pinch — try our women wire‑free bras!
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: All‑day comfort, zero pinch — try our women wire‑free bras! Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Breathable bamboo that moves with you — limited offer on men athletic briefs.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable bamboo that moves with you — limited offer on men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Shop Now

- **Campaign:** Men | Athleisure Cooling
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Breathable bamboo that moves with you — limited offer on men briefs.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable bamboo that moves with you — limited offer on men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Shop Now

- **Campaign:** Men ComfortMax Launch
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Breathable bamboo that moves with you — limited offer on men inner vests.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable bamboo that moves with you — limited offer on men inner vests. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men  Premium  Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Breathable bamboo that moves with you — limited offer on men inner vests.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable bamboo that moves with you — limited offer on men inner vests. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women  Summer  Invisible
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Breathable bamboo that moves with you — limited offer on women bras.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable bamboo that moves with you — limited offer on women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN  Seamless  Everyday
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Breathable bamboo that moves with you — limited offer on women bras.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable bamboo that moves with you — limited offer on women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Breathable bamboo that moves with you — limited offer on women panties.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable bamboo that moves with you — limited offer on women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Try It Today

- **Campaign:** MEN SIGNATURE SOFT
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Breathable cotton that moves with you — limited offer on men athletic briefs.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable cotton that moves with you — limited offer on men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Grab the Offer

- **Campaign:** WOMEN Cotton Classics
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Breathable cotton that moves with you — limited offer on women sports bras.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable cotton that moves with you — limited offer on women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men  Premium  Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Breathable microfiber that moves with you — limited offer on men inner vests.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable microfiber that moves with you — limited offer on men inner vests. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Grab the Offer

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Breathable microfiber that moves with you — limited offer on women boyshorts.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable microfiber that moves with you — limited offer on women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN  Cotton  Classics
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Breathable microfiber that moves with you — limited offer on women bras.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable microfiber that moves with you — limited offer on women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Shop Now

- **Campaign:** WOEN  Cotton  Classics
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Breathable microfiber that moves with you — limited offer on women sports bras.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable microfiber that moves with you — limited offer on women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Try It Today

- **Campaign:** Women-Studio Sports
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Breathable microfiber that moves with you — limited offer on women wire‑free bras.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable microfiber that moves with you — limited offer on women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Breathable modal that moves with you — limited offer on men briefs.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable modal that moves with you — limited offer on men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN_Seamless_Everyday
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Breathable organic cotton that moves with you — limited offer on women sports bras.
  - New headline: Premium Comfort, Now at an Irresistible Price
  - New primary text: Breathable organic cotton that moves with you — limited offer on women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without...
  - CTA suggestion: Explore Collection

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Confidence starts inside — elevate with men boxers.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with men boxers. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Explore Collection

- **Campaign:** Men | Athleisure Cooling
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Confidence starts inside — elevate with men trunks.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with men trunks. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men_Premium_Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Confidence starts inside — elevate with men trunks.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with men trunks. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Confidence starts inside — elevate with women boyshorts.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** WOMEN SEAMLESS EVERYDAY
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Confidence starts inside — elevate with women boyshorts.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** women | studio sports
  - Audience Type: Retargeting
  - Platform: Facebook
  - Old message: Confidence starts inside — elevate with women boyshorts.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN Cotton Classics
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Confidence starts inside — elevate with women bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN_Seamless_Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Confidence starts inside — elevate with women panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN_Cotton_Classics
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Confidence starts inside — elevate with women panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** women_Summer_Invisible
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Confidence starts inside — elevate with women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Confidence starts inside — elevate with women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN SUMMER INVISIBLE
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Confidence starts inside — elevate with women wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women seamless-everyday
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Confidence starts inside — elevate with women wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Confidence starts inside — elevate with women wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Confidence starts inside — elevate with women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Explore Collection

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Cooling mesh panels for workouts — men briefs you’ll actually love.
  - New headline: Stay Supported Through Every Move
  - New primary text: Cooling mesh panels for workouts — men briefs you’ll actually love. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Cooling mesh panels for workouts — men briefs you’ll actually love.
  - New headline: Stay Supported Through Every Move
  - New primary text: Cooling mesh panels for workouts — men briefs you’ll actually love. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Try It Today

- **Campaign:** Men Premium Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Cooling mesh panels for workouts — men inner vests you’ll actually love.
  - New headline: Stay Supported Through Every Move
  - New primary text: Cooling mesh panels for workouts — men inner vests you’ll actually love. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN COTTON CLASSICS
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Cooling mesh panels for workouts — women boyshorts you’ll actually love.
  - New headline: Stay Supported Through Every Move
  - New primary text: Cooling mesh panels for workouts — women boyshorts you’ll actually love. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching,...
  - CTA suggestion: Try It Today

- **Campaign:** women Summer Invisible
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Cooling mesh panels for workouts — women bras you’ll actually love.
  - New headline: Stay Supported Through Every Move
  - New primary text: Cooling mesh panels for workouts — women bras you’ll actually love. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Try It Today

- **Campaign:** women Summer Invisible
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Cooling mesh panels for workouts — women panties you’ll actually love.
  - New headline: Stay Supported Through Every Move
  - New primary text: Cooling mesh panels for workouts — women panties you’ll actually love. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Grab the Offer

- **Campaign:** women Summer Invisible
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Cooling mesh panels for workouts — women panties you’ll actually love.
  - New headline: Stay Supported Through Every Move
  - New primary text: Cooling mesh panels for workouts — women panties you’ll actually love. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Cooling mesh panels for workouts — women panties you’ll actually love.
  - New headline: Stay Supported Through Every Move
  - New primary text: Cooling mesh panels for workouts — women panties you’ll actually love. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Try It Today

- **Campaign:** MEN PREMIUM MODAL
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable bamboo — meet our men trunks.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable bamboo — meet our men trunks. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women Summer Invisible
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable bamboo — meet our women panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable bamboo — meet our women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** women summer invisible
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Doctors recommend breathable bamboo — meet our women wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable bamboo — meet our women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Doctors recommend breathable cotton — meet our men briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable cotton — meet our men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women Summer Invisible
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Doctors recommend breathable cotton — meet our women boyshorts.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable cotton — meet our women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** women fit & li t
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Doctors recommend breathable cotton — meet our women boyshorts.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable cotton — meet our women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Try It Today

- **Campaign:** MEN BOLD COLORS DROP
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable microfiber — meet our men athletic briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable microfiber — meet our men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Explore Collection

- **Campaign:** Me   Premium  Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable microfiber — meet our men briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable microfiber — meet our men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** Women | Studio Sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable microfiber — meet our women bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable microfiber — meet our women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN_Seamless_Everyday
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable microfiber — meet our women panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable microfiber — meet our women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women | studio sports
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Doctors recommend breathable microfiber — meet our women panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable microfiber — meet our women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging...
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Doctors recommend breathable microfiber — meet our women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Doctors recommend breathable microfiber — meet our women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable microfiber — meet our women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Doctors recommend breathable microfiber — meet our women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Try It Today

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Doctors recommend breathable modal — meet our men athletic briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable modal — meet our men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Try It Today

- **Campaign:** Men_Bold_Colors_Drop
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Doctors recommend breathable modal — meet our men boxers.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable modal — meet our men boxers. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men Premium Modal
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Doctors recommend breathable modal — meet our men briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable modal — meet our men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** men bold colors drop
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Doctors recommend breathable modal — meet our men briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable modal — meet our men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN Cotton Classics
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Doctors recommend breathable modal — meet our women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Doctors recommend breathable modal — meet our women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN COTTON CLASSICS
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable modal — meet our women wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable modal — meet our women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men Premium Modal
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Doctors recommend breathable organic cotton — meet our men trunks.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable organic cotton — meet our men trunks. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN  Cotton  Classics
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable organic cotton — meet our women boyshorts.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable organic cotton — meet our women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Grab the Offer

- **Campaign:** Women Fit & Lift
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Doctors recommend breathable organic cotton — meet our women panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable organic cotton — meet our women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Shop Now

- **Campaign:** women Summer Invisible
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Doctors recommend breathable organic cotton — meet our women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Doctors recommend breathable organic cotton — meet our women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching,...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women Summer Invisible
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Doctors recommend breathable organic cotton — meet our women wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Doctors recommend breathable organic cotton — meet our women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without...
  - CTA suggestion: Try It Today

- **Campaign:** Men | Athleisure Cooling
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Hot & comfy: men athletic briefs now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: men athletic briefs now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Explore Collection

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Hot & comfy: men boxers now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: men boxers now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men Premium Modal
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Hot & comfy: men boxers now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: men boxers now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** men bld colors drop
  - Audience Type: Retargeting
  - Platform: Facebook
  - Old message: Hot & comfy: men briefs now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: men briefs now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men | Athleisure Cooling
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Hot & comfy: men inner vests now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: men inner vests now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men Premium Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Hot & comfy: men trunks now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: men trunks now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN  Seamless  Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Hot & comfy: women bras now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: women bras now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN Cotton Classics
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Hot & comfy: women bras now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: women bras now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women cotton classics
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Hot & comfy: women panties now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: women panties now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women Summer Invisible
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Hot & comfy: women sports bras now 20% off — feel the difference.
  - New headline: Stay Supported Through Every Move
  - New primary text: Hot & comfy: women sports bras now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Hot & comfy: women sports bras now 20% off — feel the difference.
  - New headline: Stay Supported Through Every Move
  - New primary text: Hot & comfy: women sports bras now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Hot & comfy: women wire‑free bras now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: women wire‑free bras now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN  Seamless  Everyday
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Hot & comfy: women wire‑free bras now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: women wire‑free bras now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching,...
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN SEAMLESS EVERYDAY
  - Audience Type: Retargeting
  - Platform: Facebook
  - Old message: Hot & comfy: women wire‑free bras now 20% off — feel the difference.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Hot & comfy: women wire‑free bras now 20% off — feel the difference. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** MEN COMFORTMA LAUNCH
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Invisible under tees — seamless men briefs.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Invisible under tees — seamless men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men ComfortMax Launch
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Invisible under tees — seamless men trunks.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Invisible under tees — seamless men trunks. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN_Seamless_Everyday
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Invisible under tees — seamless women boyshorts.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Invisible under tees — seamless women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Grab the Offer

- **Campaign:** Women Summer Invisible
  - Audience Type: Retargeting
  - Platform: Facebook
  - Old message: Invisible under tees — seamless women boyshorts.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Invisible under tees — seamless women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or constant...
  - CTA suggestion: Explore Collection

- **Campaign:** women_Summer_Invisible
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Invisible under tees — seamless women bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Invisible under tees — seamless women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Shop Now

- **Campaign:** Women Cotton Classics
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Invisible under tees — seamless women bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Invisible under tees — seamless women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or constant readjusting.
  - CTA suggestion: Explore Collection

- **Campaign:** women | studio sports
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Invisible under tees — seamless women sports bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Invisible under tees — seamless women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women seamless everyday
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Invisible under tees — seamless women wire‑free bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Invisible under tees — seamless women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or constant...
  - CTA suggestion: Explore Collection

- **Campaign:** Men | Athleisure Cooling
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: No ride‑up guarantee — best‑selling men boxers back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling men boxers back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men Premium Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: No ride‑up guarantee — best‑selling men inner vests back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling men inner vests back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** Women Cotton Classics
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: No ride‑up guarantee — best‑selling women bras back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women bras back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN | STUDIO SPORTS
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: No ride‑up guarantee — best‑selling women panties back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women panties back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** women | studio sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: No ride‑up guarantee — best‑selling women panties back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women panties back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Explore Collection

- **Campaign:** women | studio sports
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: No ride‑up guarantee — best‑selling women panties back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women panties back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: No ride‑up guarantee — best‑selling women sports bras back in stock.
  - New headline: Stay Supported Through Every Move
  - New primary text: No ride‑up guarantee — best‑selling women sports bras back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching,...
  - CTA suggestion: Shop Now

- **Campaign:** Women | Studio Sports
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: No ride‑up guarantee — best‑selling women sports bras back in stock.
  - New headline: Stay Supported Through Every Move
  - New primary text: No ride‑up guarantee — best‑selling women sports bras back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching,...
  - CTA suggestion: Try It Today

- **Campaign:** Women_|_Studio_Sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: No ride‑up guarantee — best‑selling women wire‑free bras back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women wire‑free bras back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Grab the Offer

- **Campaign:** women seamless everyday
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: No ride‑up guarantee — best‑selling women wire‑free bras back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women wire‑free bras back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching,...
  - CTA suggestion: Explore Collection

- **Campaign:** women  Summer  Invisible
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: No ride‑up guarantee — best‑selling women wire‑free bras back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women wire‑free bras back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching,...
  - CTA suggestion: Try It Today

- **Campaign:** women  Summer  Invisible
  - Audience Type: Retargeting
  - Platform: Facebook
  - Old message: No ride‑up guarantee — best‑selling women wire‑free bras back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women wire‑free bras back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN Cotton Classics
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: No ride‑up guarantee — best‑selling women wire‑free bras back in stock.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: No ride‑up guarantee — best‑selling women wire‑free bras back in stock. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Explore Collection

- **Campaign:** men bold colors drop
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Push comfort, not wires — everyday men briefs.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Grab the Offer

- **Campaign:** MEN Signature Soft
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Push comfort, not wires — everyday men inner vests.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday men inner vests. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Explore Collection

- **Campaign:** Men Comfortmax Launch
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Push comfort, not wires — everyday men inner vests.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday men inner vests. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** Men_Premium_Modal
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Push comfort, not wires — everyday men inner vests.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday men inner vests. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Women | Studio Sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Push comfort, not wires — everyday women bras.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN  Seamless  Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Push comfort, not wires — everyday women panties.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Grab the Offer

- **Campaign:** WOMEN SUMMER INVISIBLE
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Push comfort, not wires — everyday women sports bras.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** women cotton classics
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Push comfort, not wires — everyday women wire‑free bras.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** Women | Studio Sports
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Push comfort, not wires — everyday women wire‑free bras.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Push comfort, not wires — everyday women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Seamless confidence for every day — new men athletic briefs.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Explore Collection

- **Campaign:** Men ComfortMax Launch
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Seamless confidence for every day — new men athletic briefs.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Try It Today

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Seamless confidence for every day — new men athletic briefs.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men ComfortMax Launch
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Seamless confidence for every day — new men boxers.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new men boxers. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Seamless confidence for every day — new women boyshorts.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** women cotton classics
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Seamless confidence for every day — new women bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** Women_|_Studio_Sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Seamless confidence for every day — new women bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Seamless confidence for every day — new women bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** Women_|_Studio_Sports
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Seamless confidence for every day — new women bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** Women | Studio Sports
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Seamless confidence for every day — new women wire‑free bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** Women Seamless Everyday
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Seamless confidence for every day — new women wire‑free bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Women_|_Studio_Sports
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Seamless confidence for every day — new women wire‑free bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Women Summer Invisible
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Seamless confidence for every day — new women wire‑free bras.
  - New headline: Seamless Support You’ll Never Feel—but Always Notice
  - New primary text: Seamless confidence for every day — new women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men  Bold  Colors  Drop
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable men athletic briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Stretch that snaps back — durable men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable men boxers.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Stretch that snaps back — durable men boxers. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Shop Now

- **Campaign:** MEN Signature Soft
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable men briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Stretch that snaps back — durable men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** MEN Signature Soft
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable men trunks.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Stretch that snaps back — durable men trunks. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant readjusting.
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN_Seamless_Everyday
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable women boyshorts.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Stretch that snaps back — durable women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** Women Seamless Everyday
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable women bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Stretch that snaps back — durable women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant readjusting.
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN COTTON CLASSICS
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Stretch that snaps back — durable women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Stretch that snaps back — durable women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** Women-Studio Sports
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Stretch that snaps back — durable women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** Women  |  Studio  Sports
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Stretch that snaps back — durable women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** Women_|_Studio_Sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable women wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Stretch that snaps back — durable women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN_Seamless_Everyday
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Stretch that snaps back — durable women wire‑free bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Stretch that snaps back — durable women wire‑free bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Summer‑ready essentials — sweat‑wicking men athletic briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Summer‑ready essentials — sweat‑wicking men athletic briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Explore Collection

- **Campaign:** Men Premium Modal
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Summer‑ready essentials — sweat‑wicking men boxers.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Summer‑ready essentials — sweat‑wicking men boxers. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** MEN  Signature  Soft
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Summer‑ready essentials — sweat‑wicking men briefs.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Summer‑ready essentials — sweat‑wicking men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN SUMMER INVISIBLE
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Summer‑ready essentials — sweat‑wicking women bras.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Summer‑ready essentials — sweat‑wicking women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN  Cotton  Classics
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Summer‑ready essentials — sweat‑wicking women panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Summer‑ready essentials — sweat‑wicking women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** WOMEN Cotton Classics
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Summer‑ready essentials — sweat‑wicking women panties.
  - New headline: Innerwear That Feels as Good as It Looks
  - New primary text: Summer‑ready essentials — sweat‑wicking women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN_Cotton_Classics
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Summer‑ready essentials — sweat‑wicking women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Summer‑ready essentials — sweat‑wicking women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Try It Today

- **Campaign:** women  Summer  Invi ible
  - Audience Type: Lookalike
  - Platform: Instagram
  - Old message: Summer‑ready essentials — sweat‑wicking women sports bras.
  - New headline: Stay Supported Through Every Move
  - New primary text: Summer‑ready essentials — sweat‑wicking women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** men comfortmax launch
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Ultra‑soft waistband, no marks — premium men boxers.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium men boxers. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** MEN BOLD COLORS DROP
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Ultra‑soft waistband, no marks — premium men briefs.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** Men Bold Colors Drop
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Ultra‑soft waistband, no marks — premium men briefs.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium men briefs. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or constant...
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Ultra‑soft waistband, no marks — premium women boyshorts.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium women boyshorts. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Shop Now

- **Campaign:** women seamless everyday
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Ultra‑soft waistband, no marks — premium women bras.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium women bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Women | Studio Sports
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Ultra‑soft waistband, no marks — premium women panties.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium women panties. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** women_Summer_Invisible
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Ultra‑soft waistband, no marks — premium women sports bras.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or constant...
  - CTA suggestion: Grab the Offer

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Lookalike
  - Platform: Facebook
  - Old message: Ultra‑soft waistband, no marks — premium women sports bras.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for lookalike, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** women summer invisible
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Ultra‑soft waistband, no marks — premium women sports bras.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Ultra‑soft waistband, no marks — premium women sports bras. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Grab the Offer

- **Campaign:** MEN BOLD COLORS DROP
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Wire‑free ease, cloud‑soft cups — men athletic briefs that fits right.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Wire‑free ease, cloud‑soft cups — men athletic briefs that fits right. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men Premium Modal
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Wire‑free ease, cloud‑soft cups — men boxers that fits right.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Wire‑free ease, cloud‑soft cups — men boxers that fits right. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** Men ComfortMax Launch
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Wire‑free ease, cloud‑soft cups — men trunks that fits right.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Wire‑free ease, cloud‑soft cups — men trunks that fits right. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching, digging or...
  - CTA suggestion: Shop Now

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Wire‑free ease, cloud‑soft cups — women panties that fits right.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Wire‑free ease, cloud‑soft cups — women panties that fits right. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Upgrade Your Comfort

- **Campaign:** WOMEN_Cotton_Classics
  - Audience Type: Broad
  - Platform: Instagram
  - Old message: Wire‑free ease, cloud‑soft cups — women panties that fits right.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Wire‑free ease, cloud‑soft cups — women panties that fits right. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging or...
  - CTA suggestion: Try It Today

- **Campaign:** Women Fit & Lift
  - Audience Type: Broad
  - Platform: Facebook
  - Old message: Wire‑free ease, cloud‑soft cups — women wire‑free bras that fits right.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Wire‑free ease, cloud‑soft cups — women wire‑free bras that fits right. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for broad, without pinching, digging...
  - CTA suggestion: Explore Collection

- **Campaign:** WOMEN Seamless Everyday
  - Audience Type: Retargeting
  - Platform: Instagram
  - Old message: Wire‑free ease, cloud‑soft cups — women wire‑free bras that fits right.
  - New headline: All-Day Soft Comfort for Everyday Confidence
  - New primary text: Wire‑free ease, cloud‑soft cups — women wire‑free bras that fits right. Upgrade to soft, breathable fabric that stays invisible under clothes and comfortable all day long. Designed for retargeting, without pinching,...
  - CTA suggestion: Upgrade Your Comfort

## 5. Suggested Next Actions
- Test 2–3 new creatives per fatigued audience/creative cluster.
- Shift spend towards high-ROAS platforms and audiences.
- Monitor ROAS, CTR and frequency over the next 7–14 days post-changes.
