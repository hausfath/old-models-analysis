**Contents**

A)	Overview  ……………………..…………………………………………………….………..	1  
B)	Search procedure for studies  ……………………………………………………….………..	1  
C)	Study inclusion and exclusion criteria  . …………………….……………….…….….……..	1  
D)	Projection inclusion and exclusion criteria   ……….………………………………….…….	2  
E)	Generating time series for projected forcing and temperature  ………..……………….……	3  
F)	Excluded pre-1970 studies and iTCR estimates …...…………………….…….……..…...…	4  
G)	Included sources and projections ……………………………………………….…….…...…	5  
H)	References  …………………………………………………………………………….……	19

**A) Overview**

Prior research assessed projections of the global mean surface temperature (GMST) trend and the ratio of GMST change versus forcing.[1–8](https://www.zotero.org/google-docs/?FdmdnK) The latter ratio was quantified as implied transient climate response (iTCR).[1–3](https://www.zotero.org/google-docs/?E8I9LS) These assessments excluded relevant projections published before 1970\. We therefore systematically searched the literature to identify additional GMST and forcing projections. Annual time series for GMST and forcing were then generated for each projection. Time series, analyses, and code are available at: [https://github.com/hausfath/old-models-analysis](https://github.com/hausfath/old-models-analysis).

Section B details the procedure for the literature search. Section C specifies inclusion criteria for studies. Section D specifies inclusion criteria for projections. Section E states methods for generating annual GMST and forcing time series. Section F lists pre-1970 analyses that did not pass our inclusion criteria, but for which iTCR could be calculated. Section G lists the included studies and projections.

**B) Search procedure for studies**

Studies were identified through personal correspondence and works cited in seven reviews.[1, 9–14](https://www.zotero.org/google-docs/?DqUy8u) Eight other assessments were also reviewed for projections.[5, 8, 15–20](https://www.zotero.org/google-docs/?3oFhGv) Additional studies were identified by searching Google Scholar for “*carbon dioxide, global warming*”, “*greenhouse effect, climate warming*”, and similar variations.[21](https://www.zotero.org/google-docs/?tq6eil) If studies identified in this search cited projections from other sources, then those sources were also reviewed for inclusion.

**C) Study inclusion and exclusion criteria**

We included all studies from a prior assessment of academic projections.[1](https://www.zotero.org/google-docs/?mx2yaT) Consistent with this prior assessment, we excluded studies:

* from non-academic and non-governmental sources such as industry,[2](https://www.zotero.org/google-docs/?8FqDz4) media,[22, 23](https://www.zotero.org/google-docs/?DwtSTR) and non-profit organizations[24](https://www.zotero.org/google-docs/?GiU9Ee)  
* that included only estimates of equilibrium warming with no defined time frame[25–27](https://www.zotero.org/google-docs/?AE1GXk)

We included studies that met all of the following criteria:

* written in English or readily translatable to English[28, 29](https://www.zotero.org/google-docs/?xEksMg)  
* published before 1994, to coincide with the time frame assessed in a prior publication[1](https://www.zotero.org/google-docs/?5kJgPa)  
* from an academic source[1](https://www.zotero.org/google-docs/?4WCBcj) such as a peer-reviewed journal article, conference anthology, or report co-authored for the government by academics  
* specified a future time frame for quantified changes in greenhouse gas concentration, forcing, or GMST, such as by specifying an end year or rate of GMST increase per year  
* fulfilled at least one of the following three requirements:  
* a) projected GMST change, and b) projected greenhouse gas concentration change or projected forcing  
* a) projected a ratio of GMST change versus greenhouse gas concentration change, and b) projected GMST change or projected greenhouse gas concentration change  
* a) projected a ratio of GMST change versus forcing, and b) projected GMST change or projected forcing

Studies presenting the same projection were addressed as follows:  
 

* If a review paper summarized projections from other sources without endorsing the projections as accurate, then the review paper was included if it was the only publicly accessible source for at least one of the projections. The review was otherwise excluded to prevent inclusion of identical projections.  
* If publications from the same author group endorsed the same projection, then only the earliest publication was included. This exclusion prevented an author group from dominating our analysis.  
* If publications from different author groups endorsed the same projection, then each publication was included. This inclusion highlighted influential projections.  
* If a publication only repeated projections from the Intergovernmental Panel on Climate Change (IPCC), then the publication was excluded. These publications were not informative because it is already known that IPCC projections influenced the scientific literature.

**D) Projection inclusion and exclusion criteria**

Prior analyses included multiple projections from the same study.[1, 2](https://www.zotero.org/google-docs/?Vu8NHr) Figure 1.9 of the IPCC Sixth Assessment Report instead included only one projection from each study.[3](https://www.zotero.org/google-docs/?1OJHle) We also included only one projection per study due to the large number of studies in our analysis. The criteria below determined which projection was included for studies containing multiple projections. The criteria were applied in the order they are listed, with earlier steps superseding later steps:

1. For IPCC reports we included the lower, best, and high estimates as a single projection with an uncertainty range, consistent with a prior analysis.[1](https://www.zotero.org/google-docs/?wPKzMk) This highlighted uncertainties IPCC reports synthesized from the broader literature.  
2. If the publication implied one of the projections best represented climate, then we included only that projection. The publication could state, for example, that one projection used a climate sensitivity estimate that was more realistic.  
3. If projections assumed different climate states, then we included only the state that best matched observations. If, for instance, a projection assumed increasing absolute humidity with warming and another projection assumed constant absolute humidity, then we included only the scenario with increasing absolute humidity. This allowed comparisons of projected versus observed warming to better reflect model accuracy on iTCR, instead of reflecting differences on other climate states. This criterion still permitted model error on iTCR, such as by overestimating water vapor feedback.[30](https://www.zotero.org/google-docs/?6o9vhA) A similar criterion was used in a prior assessment to select between projections from Schneider *et al*. 1981\.[1, 31](https://www.zotero.org/google-docs/?SQL5iD)  
4. If projections differed in climate sensitivity, then we merged the projections into one projection. This incorporated the projected range for sensitivity and iTCR. Projections were merged as follows:  
* For publications with exactly two or at least four projections: the projections with the least and most warming were the lower-range and upper-range, respectively. Median warming was calculated from that lower-range and upper-range.  
* For publications with exactly three projections: the projection with the least warming was the lower-range, the projection with intermediate warming was the average, and the projection with the most warming was the upper-range.  
5. If projections differed in precision, then we included only the projection with the most precise iTCR. This permitted better assessment of iTCR accuracy. Less precision could be due to a wider range for projected greenhouse gas increases or for GMST increases.  
6. If projections differed in projected forcing, then we included only the projection whose forcing increase best matched observations. This criterion led to inclusion of scenario B from Hansen *et al*. 1988, the same scenario included in figure 1.9 of the IPCC Sixth Assessment Report.[3, 32](https://www.zotero.org/google-docs/?iMUi68) This criterion allowed comparisons of observed versus projection warming to better reflect model accuracy on iTCR instead of reflecting differences in greenhouse gas increases. These differences in greenhouse gas increases could result from factors such as policy choices instead of model accuracy.[1](https://www.zotero.org/google-docs/?zQBOtN) 

**E) Generating time series for projected forcing and temperature**

We generated a time series of annual values of projected forcing and of projected GMST for each projection. The projection start year was taken from the publication, or the publication year if the publication stated no start year.[1](https://www.zotero.org/google-docs/?s2f6H3) The projection end year was the year stated by the publication, or 2024 if the publication stated an end year after 2024\.

If the publication provided a graph of projected annual greenhouse gas concentrations, forcing, or GMST, then we generated time series from the digitized graph.[33](https://www.zotero.org/google-docs/?z7Upc5) If the publication provided no graph nor equation for projected annual forcing, then annual forcing was inferred from projected greenhouse gas increases using previously published methods[1](https://www.zotero.org/google-docs/?AtchDS) and radiative efficiencies from table 8.A.1 of the IPCC Fifth Assessment Report.[34](https://www.zotero.org/google-docs/?eNEZe1) Gases lacking radiative efficiency estimates were excluded from our analysis. This exclusion did not substantially change any of the annual time series. If the publication provided no equation nor graph for projected annual GMST change, then GMST change was interpolated from projected forcing, consistent with previously published methods.[1](https://www.zotero.org/google-docs/?eEHmt0)

**F) Excluded pre-1970 studies and iTCR estimates**

Published assessments of projected iTCR did not include projections published before 1970\.[1–3](https://www.zotero.org/google-docs/?ifkXul) This section therefore reviews iTCR estimates published before 1970, focusing on studies that did not pass the inclusion criteria in section C. These publications were excluded due to not projecting future forcing and GMST change within a defined time frame. The studies, however, provided sufficient information for calculating assumed forcing and iTCR using previously published methods.[1](https://www.zotero.org/google-docs/?zUr5dv) Greenhouse gas increases, forcing, GMST change, and iTCR estimates are listed below for these studies.

1) Mitchell 1961[35](https://www.zotero.org/google-docs/?ihopXf)  
- greenhouse gases: 14% CO2 increase from 287 ppm to 326 ppm (figure 6B and page 243)  
- forcing: 0.68 Wm\-2  
- GMST: 0.5°F (page 244\)   
- iTCR: 1.5°C

2) MacDonald 1966[36](https://www.zotero.org/google-docs/?vPxWVY)  
- greenhouse gases: 15%, 12.5%, and 10% CO2 increase (lower-range, average, and upper-range, respectively; page 10\)  
- forcing: 0.75, 0.63, and 0.51 Wm\-2 (lower-range, average, and upper-range, respectively)  
- GMST: 0.2°C (page 10\)  
- iTCR: 1.2°C \[1.0°C \- 1.5°C\]

3) Malone 1967[37](https://www.zotero.org/google-docs/?ubLisU)  
- greenhouse gases: 15%, 12.5%, and 10% CO2 increase (lower-range, average, and upper-range, respectively; page 899\)  
- forcing: 0.75, 0.63, and 0.51 Wm\-2 (lower-range, average, and upper-range, respectively)  
- GMST: 0.2°C (page 899\)  
- iTCR: 1.2°C \[1.0°C \- 1.5°C\]

4) Ohring 1967[38](https://www.zotero.org/google-docs/?dZSKwk)  
- greenhouse gases: 10%, 12.5%, and 15% CO2 increase (lower-range, average, and upper-range, respectively; page 11\)  
- forcing: 0.51, 0.63, and 0.75 Wm\-2 (lower-range, average, and upper-range, respectively)  
- GMST: 0.1°C, 0.15°C, and 0.2°C (lower-range, average, and upper-range, respectively; page 11\)  
- iTCR: 0.9°C \[0.7°C \- 1.0°C\]

These iTCR estimates can be compared to a TCR best estimate of 1.8°C from the IPCC Sixth Assessment Report. The likely and very likely ranges (66% \- 100% and 90% \- 100%, respectively) for this IPCC estimate were 1.4°C \- 2.2°C and 1.2°C \- 2.4°C, respectively.[3](https://www.zotero.org/google-docs/?mVBK50) Other assessments supported a similar TCR[39, 40](https://www.zotero.org/google-docs/?lVZNyr) and iTCR range.[1, 2](https://www.zotero.org/google-docs/?6D4ulX) Observational evidence also supported the forcing estimates used in calculating this iTCR range.[41](https://www.zotero.org/google-docs/?YG1rMF) Some projected TCRs[42, 43](https://www.zotero.org/google-docs/?u3LgfI) and iTCRs[1, 2](https://www.zotero.org/google-docs/?W98GDH) conflicted with this observational range. This contradicts suggestions that forcing estimates entail alignment between observed versus projected iTCR.[21, 44](https://www.zotero.org/google-docs/?dHY7WW)

**G) Included sources and projections**

Time series for projected forcing and GMST change were generated from each study using section D, section E, and the information listed below.

1) Arrhenius 1896,[45](https://www.zotero.org/google-docs/?6SMfYG) as translated in Rodhe 1997[46](https://www.zotero.org/google-docs/?agzLQa)  
- forcing: 1896-4896 linear 2.17 Wm\-2 increase from a 50% CO2 increase (page 4 of Rodhe 1997\)  
- GMST: 1896-4896 linear 3.4°C increase (page 4\) 

2) Callendar 1938[47](https://www.zotero.org/google-docs/?OQBixe)  
- forcing: 1920-2024 linear interpolation between CO2 values in tables I and VI  
- GMST: 1920-2024 linear interpolation between values in table VI

3) Plass 1953,[48](https://www.zotero.org/google-docs/?8yB2VI) summarized in Northcott 1953[49](https://www.zotero.org/google-docs/?tg09uf) and Hewson 1953[50](https://www.zotero.org/google-docs/?cQ2bfz)  
1. 50% CO2 increase implies ‘2.2°C / 2.17 Wm\-2’ (table 2 of Hewson 1953\)  
2. 1953-2080 CO2 increase of 100% implies 3.71 Wm\-2 (page 260 of Northcott 1953\)  
3. 3.71 Wm\-2 for 1953-2080 multiplied by ‘2.2°C / 2.17 Wm\-2’ implies 3.8°C (page 260 of Northcott 1953\)  
- forcing: 1953-2080 linear 3.71 Wm\-2 increase  
- GMST: 1953-2080 linear 3.8°C increase

4) Plass 1956[51](https://www.zotero.org/google-docs/?lC2k3A)  
- forcing: 1900-2000 linear 1.40 Wm\-2 increase from a 30% CO2 increase (page 149\)  
- GMST: 1900-2000 linear 1.1°C increase (page 149\)

5) Plass 1959,[52](https://www.zotero.org/google-docs/?Rp9xQz) summarized in Hepting 1963[53](https://www.zotero.org/google-docs/?h579zL)  
1. 1860-1952 CO2 increase of 284 ppm to 322 ppm implies ‘0.67 Wm\-2 / 1°F’ (pages 43 and 46 of Plass 1959\)  
2. 3.6°F for 1860-2000 multiplied by ‘0.67 Wm\-2 / 1°F’ implies 2.42 Wm\-2 (page 46\)  
3. 2.42 Wm\-2 for 1860-2000 and 284 ppm in 1860 implies 446 ppm in 2000  
4. 1952-2000 CO2 increase of 322 ppm to 446 ppm implies 1.74 Wm\-2  
5. 1°F for 1860-1952 and 3.6°F for 1860-2000 implies 2.6°F (1.4°C) for 1952-2000  
- forcing: 1952-2000 linear 1.74 Wm\-2 increase  
- GMST: 1952-2000 linear 1.4°C increase

6) Kondratiev 1960[54](https://www.zotero.org/google-docs/?LIF5il)  
1. 1860-1960 CO2 increase of 10% implies 0.51 Wm\-2 (page 226\)  
2. CO2 doubling implies ‘0.5°C / 3.71 Wm\-2’ (page 226\)  
3. 0.51 Wm\-2 for 1860-1960 multiplied by ‘0.5°C / 3.71 Wm\-2’ implies 0.07°C, matching transient warming of “*less than 0.1°*” (page 226\)  
4. lower: 1960-2000 CO2 increase of 6% implies 0.31 Wm\-2 (page 224\)  
5. upper: 1960-2000 CO2 increase of 9% implies 0.46 Wm\-2 (page 224\)  
6. lower: 0.31 Wm\-2 for 1960-2000 multiplied by ‘0.5°C / 3.71 Wm\-2’ implies 0.042°C  
7. upper: 0.46 Wm\-2 of 1960-2000 multiplied by ‘0.5°C / 3.71 Wm\-2’ implies 0.062°C  
- forcing: 1960-2000 linear increase of 0.31 and 0.46 Wm\-2 (lower- and upper-range, respectively)  
- GMST: 1960-2000 linear increase of 0.042 and 0.062°C (lower- and upper range, respectively)

7) Wilkins 1961[55](https://www.zotero.org/google-docs/?HY1KRU)  
- greenhouse gases: 1961-2024 linear 1.4 ppm/year CO2 increase from 319 ppm (page 1314\)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1961-2024 linear increase of 0.6 and 1.1°C/century (lower- and upper-range, respectively; page 1314\)

8) President’s Science Advisory Committee 1965[30](https://www.zotero.org/google-docs/?vGHTtV)  
- greenhouse gases: 1860-2020 non-linear CO2 increase of 25% from 300 ppm to 375 ppm (tables 3 and 6; pages 115, 116, and 119-120)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1860-2020 linear interpolation from forcing for 4°C (page 121\)

9) Sargent 1967[56](https://www.zotero.org/google-docs/?4Sda0g)  
1. 1.6°C for 1900-1967 and 4°C for 1900-2000 implies 2.4°C for 1967-2000 (page 693\)  
2. lower: 1900-1967 CO2 increase of 25% implies ‘1.2 Wm\-2 / 1.6°C’ (page 693\)  
3. average: 1900-1967 CO2 increase of 20% implies ‘0.98 Wm\-2 / 1.6°C’ (page 693\)  
4. upper: 1900-1967 CO2 increase of 15% implies ‘0.75 Wm\-2 / 1.6°C’ (page 693\)  
5. lower: 2.4°C for 1967-2000 multiplied by ‘1.2 Wm\-2 / 1.6°C’ implies 1.79 Wm\-2  
6. average: 2.4°C for 1967-2000 multiplied by ‘0.98 Wm\-2 / 1.6°C’ implies 1.46 Wm\-2  
7. upper: 2.4°C for 1967-2000 multiplied by ‘0.75 Wm\-2 / 1.6°C’ implies 1.12 Wm\-2  
- forcing: 1967-2000 linear increase of 1.79, 1.46, and 1.12 Wm\-2 (lower-range, average, and upper-range, respectively)  
- GMST: 1967-2000 linear 2.4°C increase

10) Fletcher 1969,[57](https://www.zotero.org/google-docs/?I6WknD) summarized in Rand Corporation 1969[58](https://www.zotero.org/google-docs/?zjHvU8)  
1. lower: 1900-1969 CO2 increase of 15% implies ‘0.75 Wm\-2 / 0.5°C’ (page 2 of Fletcher 1969\)  
2. average: 1900-1969 CO2 increase of 12.5% implies ‘0.63 Wm\-2 / 0.5°C’ (page 2\)  
3. upper: 1900-1969 CO2 increase of 10% implies ‘0.51 Wm\-2 / 0.5°C’ (page 2\)  
4. lower: 1.5°C for 1969-2000 multiplied by ‘0.75 Wm\-2 / 0.5°C’ implies 2.24 Wm\-2  
5. average: 1.5°C for 1969-2000 multiplied by ‘0.63 Wm\-2 / 0.5°C’ implies 1.89 Wm\-2  
6. upper: 1.5°C for 1969-2000 multiplied by ‘0.51 Wm\-2 / 0.5°C’ implies 1.53 Wm\-2  
- forcing: 1969-2000 linear increase of 2.24, 1.89, and 1.53 Wm\-2 (lower-range, average, and upper-range, respectively)  
- GMST: 1969-2000 linear 1.5°C increase

11) Peterson 1969[59](https://www.zotero.org/google-docs/?WKDF1D)  
1. 30% CO2 increase to 415 ppm implies 319 ppm in 1950 (page 1165; consistent with page 8 of the supporting information of Hausfather 2020[1](https://www.zotero.org/google-docs/?DHmxDr))  
2. 60% CO2 increase over 1950 levels implies 511 ppm in 2020 (page 1168\)  
3. 1950-2020 CO2 increase of 60% implies ‘3°F / 2.52 Wm\-2’ (page 1168\)  
4. 1950-1969 CO2 increase from 319 ppm to 325 ppm implies 0.096 Wm\-2 (page 1162\)  
5. 0.096 Wm\-2 for 1950-1969 multiplied by ‘3°F / 2.52 Wm\-2’ implies 0.11°F or 0.06°C  
6. 1969-2020 CO2 increase from 325 ppm to 511 ppm implies 2.42 Wm\-2 (page 1162\)  
7. 2.42 Wm\-2 for 1969-2020 multiplied by ‘3°F / 2.52 Wm\-2’ implies 2.88°F or 1.60°C  
- forcing: linear interpolation between CO2 of 319 ppm in 1950, 325 ppm in 1969, and 511 ppm in 2020  
- GMST: linear interpolation between 0°C in 1950, 0.06°C in 1969, and 1.67°C in 2020

12) Tilson 1969[60](https://www.zotero.org/google-docs/?1S5HsF)  
1. 1860-1952 CO2 increase of 284 ppm to 322 ppm implies ‘0.67 Wm\-2 / 1°F’ (page 58\)  
2. 3.6°F for 1860-2000 multiplied by ‘0.67 Wm\-2 / 1°F’ implies 2.42 Wm\-2 (page 58\)  
3. 2.42 Wm\-2 for 1860-2000 and 284 ppm in 1860 implies 446 ppm in 2000  
4. 1952-2000 CO2 increase of 322 ppm to 446 ppm implies 1.7 Wm\-2  
5. 1°F for 1860-1952 and 3.6°F for 1860-2000 implies 2.6°F (1.4°C) for 1952-2000  
- forcing: 1952-2000 linear 1.74 Wm\-2 increase  
- GMST: 1952-2000 linear 1.4°C increase

13) Austin 1970[61](https://www.zotero.org/google-docs/?bMT3e9)  
1. 10% CO2 increase implies ‘0.45°F / 0.51 Wm\-2’ (page 49\)  
2. 1970-2060 CO2 linear increase from 340 ppm to 1580 ppm implies 8.22 Wm\-2 (page 48, figure 5, and table V)  
3. 8.22 Wm\-2 for 1970-2060 multiplied by ‘0.45°F / 0.51 Wm\-2’ implies 7.3°F or 4.0°C   
- greenhouse gases: 1970-2060 CO2 linear increase from 340 ppm to 1580 ppm  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1970-2060 linear interpolation from forcing for 4.0°C

14) Barrett 1970[62](https://www.zotero.org/google-docs/?kksicX)  
- forcing: 1970-2310 linear 3.71 Wm\-2 increase from a 100% CO2 increase (page 35\)  
- GMST: 1970-2310 linear interpolation from forcing for 2°C (page 35\)

15) Benton 1970[63](https://www.zotero.org/google-docs/?LkQQrM)  
1. 10% CO2 linear increase implies ‘0.51 Wm\-2 / 0.3°C’  
2. 0.6°C for 1970-2000 multiplied by ‘0.51 Wm\-2 / 0.3°C’ implies 1.02 Wm\-2  
3. 1.02 Wm\-2 for 1970-2000 and 320 ppm in 1970 implies 387.2 ppm in 2000  
- greenhouse gases: 1970-2000 linear CO2 increase from 320 ppm to 387.2 ppm  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1970-2000 linear interpolation from forcing for 0.6°C

16) Fletcher 1970[64](https://www.zotero.org/google-docs/?oL7Y6u)  
- forcing: 1970-2000 linear 2.17 Wm\-2 increase from a 50% CO2 increase (page 44\)  
- GMST: 1970-2000 linear 1°C increase (page 44\)  
    
17) Landsberg 1970[65](https://www.zotero.org/google-docs/?7UeCZW)  
- greenhouse gases: 1970-2370 linear CO2 increase from 300 ppm to 600 ppm (page 1267\)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1970-2370 linear interpolation from forcing for 2°C (page 1267\)

18) Manabe 1970[66](https://www.zotero.org/google-docs/?lc72ht)  
- forcing: 1900-2000 linear interpolation between 300 ppm CO2 in 1900, 320 ppm in 1970, and 375 ppm in 2000 (page 27; page 8 of the supporting information of Hausfather 2020[1](https://www.zotero.org/google-docs/?U7gKra))  
- GMST: 1900-2000 linear interpolation from forcing for 0.8°C (page 28\)  
    
19) Mitchell 1970[67](https://www.zotero.org/google-docs/?ivDkI9)  
- forcing: 1969-2000 linear interpolation between CO2 values on page 144 and 320 ppm in 1969 (page 8 of the supporting information of Hausfather 2020[1](https://www.zotero.org/google-docs/?lILr2T))  
- GMST: 1969-2000 linear interpolation between values on page 145  
    
20) Presidential Council on Environmental Quality 1970[68](https://www.zotero.org/google-docs/?YN8A04)  
- forcing: 1970-2010 linear 1.19 Wm\-2 increase from 320 ppm to 400 ppm CO2 (page 1044\)  
- GMST: 1970-2010 linear 0.78°C increase (page 1044\)  
    
21) Lovelock 1971[69](https://www.zotero.org/google-docs/?RZRUSz)  
1. 325 ppm CO2 in 1969 in figure 1 implies 270.4 ppm as a baseline in figure 2  
2. 328.6 ppm CO2 in 1971 and 427.6 ppm in 2000 implies 1.41 Wm\-2 (figure 2\)  
3. 10% CO2 increase implies ‘0.3°C / 0.51 Wm\-2’ (page 403\)  
4. 1.41 Wm\-2 for 1971-2000 multiplied by ‘0.3°C / 0.51 Wm\-2’ implies 0.83°C  
- forcing: 1971-2000 linear 1.41 Wm\-2 increase from 328.6 ppm to 427.6 ppm CO2  
- GMST: 1971-2000 linear 0.83°C increase  
    
22) MacDonald 1971[70](https://www.zotero.org/google-docs/?D7zEVx)  
1. 1971-2021 CO2 increase of 314 ppm to 628 ppm implies 3.71 Wm\-2 (pages 247 and 251\)  
2. 10% CO2 increase implies ‘0.3°C / 0.51 Wm\-2’ (page 254\)  
3. 3.71 Wm\-2 for 1971-2000 multiplied by ‘0.3°C / 0.51 Wm\-2’ implies 2.2°C  
- forcing: 1971-2071 linear 3.71 Wm\-2 increase from 314 ppm to 628 ppm CO2  
- GMST: 1971-2071 linear 2.2°C increase  
    
23) Matthews 1971,[71](https://www.zotero.org/google-docs/?0oS9FU) summarized in Matthews 1973[72](https://www.zotero.org/google-docs/?FNWe2j)  
- forcing: 1971-2000 linear 0.85 Wm\-2 increase from 320 ppm to 375 ppm CO2 (page 287 of Matthews 1973\)  
- GMST: 1971-2000 linear 0.5°C increase (page 287\)

24) Rasool 1971[73](https://www.zotero.org/google-docs/?iPf53G)  
- forcing: 1970-2000 linear 0.51 Wm\-2 increase from a 10% CO2 increase (page 139\)  
- GMST: 1970-2000 linear 0.1°C increase (page 139\)  
    
25) Budyko 1972b,[74](https://www.zotero.org/google-docs/?dayDss) clarifying Budyko 1972a[75](https://www.zotero.org/google-docs/?rI6xuz)  
- forcing: 1970-2000 linear 0.75 Wm\-2 and 0.98 Wm\-2 increase from a 15% and 20% CO2 increase (upper-range and lower-range, respectively; page 19 of Budyko 1972a)  
- GMST: 1970-2000 annual values for line \#3 from figure 8 of Budyko 1972a (page 868 of Budyko 1972b)

26) Ferland 1972[76](https://www.zotero.org/google-docs/?BXgrhQ)  
1. Ferland 1972 erroneously converts ‘1.89°C for a 100% CO2 increase’ to ‘0.47°C for a 25% CO2 increase’ (page 156 of Ferland 1972; comparable to Sawyer 1972[77](https://www.zotero.org/google-docs/?CW1IAN) on page 10 of the supporting information of Hausfather 2020[1](https://www.zotero.org/google-docs/?qwLNcG))  
2. 300 ppm to 320 ppm CO2 for 1900-1970 (page 8 of the supporting information of Hausfather 2020[1](https://www.zotero.org/google-docs/?JMBVVZ))  
3. 25% increase from 300 ppm implies 375 ppm in 2000 (page 156 of Ferland 1972\)  
- forcing: 1900-2000 linear interpolation between 300 ppm CO2 in 1900, 320 ppm in 1970, and 375 ppm in 2000  
- GMST: 1900-2000 linear interpolation from forcing for 0.47°C  
    
27) Machta 1972a[78](https://www.zotero.org/google-docs/?CQLrTy)  
- greenhouse gases: 1970-2000 annual values from figure 18  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1970-2000 linear interpolation from forcing for 0.5°C (page 413\)

28) Machta 1972b[79](https://www.zotero.org/google-docs/?wrgLZu)  
- greenhouse gases: 1970-2000 annual values from figure 4  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1970-2000 linear interpolation from forcing for 0.5°C (page 21\)

29) National Science Board 1972[80](https://www.zotero.org/google-docs/?bwN2JS)  
- greenhouse gases: 25% linear CO2 increase for 1970-2020 and 80% linear CO2 increase for 1970-2270 (upper- and lower-range, respectively; pages 56 and 64\)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1970-2020 linear 1°C increase for upper-range and 1970-2270 linear 1°C increase for lower-range (pages 56 and 64\)

30) Sawyer 1972[77](https://www.zotero.org/google-docs/?FHQiEi)  
- forcing: 1969-2000 linear 1.19 Wm\-2 increase from a 25% CO2 increase from 319 ppm (pages 23 and 25\)  
- GMST: 1969-2000 linear 0.6°C increase (page 25\)  
    
31) Palmer 1973[81](https://www.zotero.org/google-docs/?BSWSZN)  
- greenhouse gases: 1970-2000 annual values from figure 2  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1970-2000 linear interpolation from forcing for 0.5°C (page 255\)

32) Landsberg 1974[82](https://www.zotero.org/google-docs/?Is765r)  
- greenhouse gases: 1974-2014 annual values from figure 6  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1974-2014 annual values from figure 6  
    
33) Barrett 1975[83](https://www.zotero.org/google-docs/?AixgHZ)  
1. 324 ppm CO2 in 1973 with a 1.06 ppm/year increase implies a 26.5 ppm increase from 326.1 ppm to 352.6 ppm for 1975-2000 (pages 33 and 37\)  
2. 26.5 ppm multiplied by 0.006°C/ ppm implies 0.16°C for 1975-2000 (page 37\)  
- greenhouse gases: 1973-2000 annual values increasing 1.06 ppm/year from 324 ppm  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1975-2000 linear interpolation from forcing for 0.16°C

34) Broecker 1975[84](https://www.zotero.org/google-docs/?GmCOCS)  
- forcing: 1970-2010 linear interpolation between CO2 values in table 1  
- GMST: 1970-2010 linear interpolation between values in table 1  
    
35) Schneider 1975[85](https://www.zotero.org/google-docs/?euOmnl)  
1. 100% CO2 increase implies ‘2°C / 3.71 Wm\-2’ and ‘3°C / 3.71 Wm\-2’ (lower- and upper-range, respectively; page 70\)  
2. 320 ppm \- 400 ppm CO2 for 1975-2000 implies 1.19 Wm\-2 (page 70 of Schneider 1975; page 8 of the supporting information of Hausfather 2020[1](https://www.zotero.org/google-docs/?6b6KFS))  
3. 1.19 Wm\-2 multiplied by ‘2°C / 3.71 Wm\-2’ and ‘3°C / 3.71 Wm\-2’ implies 0.64°C and 0.97°C for 1975-2000 (lower- and upper-range, respectively)  
4. 400 ppm \- 600 ppm CO2 for 2000-2040 implies 2.17 Wm\-2 (page 70 of Schneider 1975\)  
5. 2.17 Wm\-2 multiplied by ‘2°C / 3.71 Wm\-2’ and ‘3°C / 3.71 Wm\-2’ implies 1.17°C and 1.75°C for 1975-2000 (lower- and upper-range, respectively)  
- forcing: 1975-2040 linear interpolation between CO2 of 320 ppm in 1975, 400 ppm in 2000, and 600 ppm in 2040   
- GMST: 1975-2000 linear interpolation for 0.64°C and 0.97°C (lower- and upper-range, respectively), and 2000-2040 linear interpolation for 1.17°C and 1.75°C (lower- and upper-range, respectively)

36) United States Committee for the Global Atmospheric Research Program 1975[86](https://www.zotero.org/google-docs/?BZ6PCP)  
- forcing: 1975-2000 linear interpolation between CO2 increases of 1.8% for 1975-1980, 6.1% for 1980-1990, and 8.2% for 1990-2000 (page 43\)   
- GMST: 1975-2000 linear interpolation from forcing for 0.5°C (page 43\)  
    
37) Watts 1975[87](https://www.zotero.org/google-docs/?lw8W0H)  
1. 100% CO2 increase implies ‘1.89°C / 3.71 Wm\-2’ (page 372 of Watts 1975, page 156 of Ferland 1972[76](https://www.zotero.org/google-docs/?z0YmBH))  
2. 295 ppm to 590 ppm CO2 for 1860-2000 (page 372 of Watts 1975, page 52 of Rotty 1977[88](https://www.zotero.org/google-docs/?wLzABO))  
3. 330 ppm to 590 ppm CO2 for 1975-2000 implies 3.11 Wm\-2 (page 50 of Rotty 1977[88](https://www.zotero.org/google-docs/?InvAA0))  
4. 3.11 Wm\-2 multiplied by ‘1.89°C / 3.71 Wm\-2’ implies 1.58°C for 1975-2000  
- forcing: 1975-2000 linear 3.11 Wm\-2 increase  
- GMST: 1975-2000 linear 1.58°C increase

38) Budyko 1977[89](https://www.zotero.org/google-docs/?8h6JzG)  
1. 10% CO2 increase implies ‘0.3°C / 0.51 Wm\-2’ (page 200\)  
2. 30% \- 35% CO2 increase for 1875-2000 implies 1.40 \- 1.61 Wm\-2 (page 200\)  
3. 1.40 \- 1.61 Wm\-2 multiplied by ‘0.3°C / 0.51 Wm\-2’ implies 0.83°C \- 0.95°C  
4. 1°C for 1875-2000 implies the higher-end of 0.83°C \- 0.95°C and thus a 35% CO2 increase for 1875-2000 instead of a 30% increase (page 200\)  
5. 10% \- 15% CO2 increase for 1875-1975 and 35% increase for 1875-2000 implies 17.4% \- 22.7% increase for 1975-2000 (page 200\)  
6. 17.4% \- 22.7% CO2 increase for 1875-2000 implies 0.86 \- 1.09 Wm\-2   
7. 0.86 \- 1.09 Wm\-2 multiplied by ‘0.3°C / 0.51 Wm\-2’ implies 0.51°C \- 0.64°C  
8. 0.6°C \- 0.7°C for 1975-2000 implies the higher-end of 0.51°C \- 0.64°C and thus a 1.09 Wm\-2 increase for 1975-2000 (page 200\)  
- forcing: 1975-2000 linear 1.09 Wm\-2 increase  
- GMST: 1975-2000 linear 0.64°C increase

39) Nordhaus 1977a,[90](https://www.zotero.org/google-docs/?ExdFMQ) with Nordhaus 1977b[91](https://www.zotero.org/google-docs/?gGf81j)  
- greenhouse gases: 1974-2024 annual values from figure 9 and table 10 of Nordhaus 1977a  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1974-2024 temperature values from figure 1 of Nordhaus 1977a  
    
40) Rotty 1977[88](https://www.zotero.org/google-docs/?GTzPra)  
1. 100% CO2 increase implies ‘1.5°C / 3.71 Wm\-2’ and ‘2.4°C / 3.71 Wm\-2’ (lower- and upper-range, respectively; page 53\)  
2. 330 ppm to 600 ppm for 1975-2030 implies 3.20 Wm\-2 (pages 50 and 54\)  
3. 3.20 Wm\-2 multiplied by ‘1.5°C / 3.71 Wm\-2’ and ‘2.4°C / 3.71 Wm\-2’ implies 1.29°C and 2.07°C for 1975-2030 (lower- and upper-range, respectively):  
- forcing: 1975-2030 linear 3.20 Wm\-2 increase  
- GMST: 1975-2030 linear 1.29°C and 2.07°C increase (lower- and upper-range, respectively)

41) Kellogg 1978[92](https://www.zotero.org/google-docs/?eDn6rd)  
1. pre-industrial CO2 of 277.5 ppm, 555 ppm for 2050, 330 ppm for 1978, and 400 ppm in 2000 (page 45\)  
2. 0.5°C to 2°C of warming for 1978-2000 and 1°C to 6°C for 1978-2050, implying 0.5°C to 4°C for 2000-2050 (lower- and upper-range, respectively; pages 45 and 47\)  
- forcing: 1978-2050 linear interpolation between CO2 of 330 ppm in 1978, 400 ppm in 2000, and 555 ppm in 2050  
- GMST: 1978-2000 linear interpolation for 0.5°C and 2°C (lower- and upper-range, respectively), and 2000-2050 linear interpolation for 0.5°C and 4°C (lower- and upper-range, respectively)

42) Rotty 1978[93](https://www.zotero.org/google-docs/?JfdRfS)  
1. CO2 of 300 ppm in 1860, 315 ppm in 1958, 330 ppm in 1978, and 465 ppm in 2025 (figure 1; pages 232, 235, and 245\)  
2. 300 ppm to 465 ppm for 1860-2025 implies 2.35 Wm\-2  
3. 100% CO2 increase implies ‘1.5°C / 3.71 Wm\-2’ and ‘3°C / 3.71 Wm\-2’ (lower- and upper-range, respectively; page 239\)  
4. 2.35 Wm\-2 multiplied by ‘1.5°C / 3.71 Wm\-2’ and ‘3°C / 3.71 Wm\-2’ implies 0.95°C and 1.90°C for 1860-2025 (lower- and upper-range, respectively)  
- forcing: 1860-2025 linear interpolation between CO2 of 300 ppm in 1860, 315 ppm in 1958, 330 ppm in 1978, and 465 ppm in 2025  
- GMST: 1860-2025 linear interpolation from forcing for 0.95°C and 1.90°C (lower- and upper-range, respectively)

43) Hoyt 1979[94](https://www.zotero.org/google-docs/?uIpvHY)  
- greenhouse gases:   
- lower-range: 1860-2000 CO2 ppm equation of ‘0.00583\*(year-1880)^2 \- 0.225\*(year-1880) \+ 293’ to have a 1860-1970 9% increase from 293 ppm to 320 ppm and a 1970-2000 9% increase from 320 ppm to 350 ppm (page 390\)  
- upper-range: 1860-2000 CO2 ppm equation of ‘0.0090\*(year-1880)^2 \- 0.3656\*(year-1880) \+ 280’ to have a 1860-1970 14% increase from 280 ppm to 320 ppm and a 1970-2000 14% increase from 320 ppm to 366 ppm (page 390\)  
- forcing: calculated from annual greenhouse gas values  
- GMST:1970-2000 linear interpolation from forcing for 0.3°C and 0.4°C (lower- and upper-range, respectively; page 390\)

44) Niehaus 1979[95](https://www.zotero.org/google-docs/?podjTv)  
- greenhouse gases: 1979-2024 annual values from figure 8  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1979-2024 annual values from figure 8

45) Hoffert 1980[96](https://www.zotero.org/google-docs/?cnpMNR)  
- greenhouse gases: 1980-2000 annual values from equation 20 on page 6676  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1980-2000 annual values from figure 6a for “*Π \= 2*”, “*Π \= 1*”, and “*Π \= 0*” (lower-range, average, and upper-range, respectively)

46) Cess 1981[97](https://www.zotero.org/google-docs/?Mk0Evj)  
- forcing: 1981-2024 annual values from figure 3  
- GMST: 1981-2024 annual values from figure 4 for “*time dependent*”

47) Hansen 1981[98](https://www.zotero.org/google-docs/?rExiDn)  
- greenhouse gases: 1980-2024 “*slow growth*” in CO2 from 335 ppm (pages 963 and 964\)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1980-2024 for the “*2a*” line in figure 6  
    
48) Schneider 1981[31](https://www.zotero.org/google-docs/?tjfUK1)  
- greenhouse gases: 1981-2024 CO2 values from equation 11 on page 3138  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1981-2024 for the “*550 yr*” line in figure 3  
    
49) Gilliland 1982[99](https://www.zotero.org/google-docs/?Km5CNe)  
- forcing: 1925-2045 linear 3.71 Wm\-2 increase from 300 ppm to 600 ppm CO2 (page 113\)  
- GMST: 1925-2045 linear 1.37°C increase (page 119\)

50) Seidel 1983[100](https://www.zotero.org/google-docs/?zZbTQC)  
1. 1980 CO2 value is 339 ppm (pages C-3 and 2-8)  
2. 1980 CH4 value is 1.6ppb (page D-3)  
3. 1980 N2O value is 295ppb (pages 2-12 and D-3)  
- greenhouse gases: 1983-2024 CO2 annual values from figure 4-2 and non-CO2 annual values from table 3-4, using 1980 values of 339 ppm for CO2, 1.6ppb for CH4, and 295ppb for N2O  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1983-2024 annual values from figure 4-2

51) Hansen 1984[101](https://www.zotero.org/google-docs/?QIxe03)  
- greenhouse gases: 1980-2010 annual values from table 4  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1980-2010 annual values from figure 18 for “*k \= 2*” and “*k \= 1*” (lower- and upper-range, respectively)

52) Bach 1985[102](https://www.zotero.org/google-docs/?Z0BK4H)  
- greenhouse gases: 1980-2030 annual CO2 values from figure 2 for scenario 1  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1980-2030 linear interpolation from forcing for 1.4°C (page 43\)

53) Hoffert 1985[103](https://www.zotero.org/google-docs/?W4XMZ4)  
- greenhouse gases: 1985-2024 annual values from table 5.2 for the “*high*” equation  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1985-2024 annual values from figure 5.16A for the “*High*” scenario  
    
54) Dickinson 1986[104](https://www.zotero.org/google-docs/?tUQu9d)  
1. \~2.2 Wm\-2 from pre-industrial to 1985, with 0.5°C to 2.0°C equilibrium warming and 0.3°C to 1.0°C after correction for thermal inertia (table 2 and page 114\)  
2. lower-range: 2.2 Wm\-2 multiplied by ‘0.3°C / 2.2 Wm\-2’ implies 0.3°C for 1985-2050 (table 3\)  
3. upper-range: 7.2 Wm\-2 multiplied by ‘1.0°C / 2.2 Wm\-2’ implies 3.3°C for 1985-2050 (table 3\)  
4. 0.3°C to 3.3°C for 1985-2050 implies 0.3°C to 6.6°C after accounting for uncertainty in the thermal inertia correction (page 114\)  
5. 0.5°C for pre-industrial 1900 to 1985 and 0.3°C to 6.6°C for 1985-2050 implies 0.8°C to 7.1°C for pre-industrial 1900 to 2050 (page 114\)  
6. 0.8°C to 7.1°C for pre-industrial 1900 to 2050 parallels to “*1 °C to \>5 °C*”, updating the range to 1°C to 7.1°C for 1900-2050 (page 114\)  
7. 0.5°C for 1900-1985 subtracted from 1°C to 7.1°C for 1900-2050 implies 0.5°C to 6.6°C for 1985-2050  
- forcing: 1985-2050 linear 2.2 and 7.2 Wm\-2 increase (lower- and upper-range, respectively)  
- GMST: 1985-2050 linear 0.5°C and 6.6°C increase (lower- and upper-range, respectively)

55) Jones 1987[105](https://www.zotero.org/google-docs/?yl4aq3)  
- greenhouse gases: 1987-2024 annual values from figure 2 for the dashed line  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1987-2024 annual values from figure 3 for the middle line  
    
56) Peng 1987[106](https://www.zotero.org/google-docs/?FcpE5B)  
- greenhouse gases: 1987-2024 annual values from figure 15  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1987-2024 annual values from figure 18 for the lower and higher “*TRANSIENT*” lines (lower- and upper-range, respectively)

57) Ramanathan 1987a[107](https://www.zotero.org/google-docs/?LxHXBk)  
- greenhouse gases: 1987-2024 CO2 and non-CO2 annual values from tables 10 and 11 for “*Case B*”  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1987-2024 annual values from figure 27b for the two dotted lines (lower-range and upper-range)

58) Ramanathan 1987b[108](https://www.zotero.org/google-docs/?dOJSgW)  
- forcing: linear forcing increase between the 1980 and 2030 CO2 and non-CO2 values in figure 16.2 on pages 242 and 243, with values for “*Possible Range*” being the lower-range and upper-range; exclude NH3, NO, NO2, CSO, CS2, SO2, H2S, C2HCl3, C2Cl4, CH2BrCH2Br, CH2I, C2H6, C2H2, C3H8, CO, H2, tropospheric ozone, HCHO, and CH3CHO  
- GMST: 1980-2030 linear 1°C and 2.5°C increase (lower- and upper-range, respectively; figure 16.2 on page 243\)

59) Tricot 1987[109](https://www.zotero.org/google-docs/?kNTiLV)  
- greenhouse gases: 1987-2024 annual values from figure 2a for “*low*”, with figures 2b-2d   
- forcing: calculated from annual greenhouse gas values, using 0.699 Wm\-2ppb\-1 radiative efficiency for CFCs in figure 2d (equation 5 on page 46; table 8.A.1 of IPCC 2013[34](https://www.zotero.org/google-docs/?QQjf69))  
- GMST: 1987-2024 annual values from figure 13 for “*low*”  
    
60) Wigley 1987[110](https://www.zotero.org/google-docs/?iV08XB)  
- forcing: 1985-2025 annual values from figure 1 for 67% of “*Intermediate*”, “*Intermediate*”, and 150% of “*Intermediate*” (lower-range, average, and upper-range, respectively; page 130\)  
- GMST: 1985-2025 linear interpolation from forcing for 0.47°C, 0.80°C, and 1.80°C (lower-range, average, and upper-range, respectively; pages 130-131)  
    
61) Hansen 1988[32](https://www.zotero.org/google-docs/?4empdp)  
- forcing: obtained from the NASA Goddard Institute for Space Studies for scenario B[1](https://www.zotero.org/google-docs/?UI8yTE)  
- GMST: obtained from the NASA Goddard Institute for Space Studies for scenario B[1, 8](https://www.zotero.org/google-docs/?AUgTc1)

62) MacDonald 1988[111](https://www.zotero.org/google-docs/?cjONWo)  
- forcing: 1980-2030 linear interpolation between CO2 and non-CO2 values in table 1, with the lower-range as the smaller increase and the upper-range as the larger increase; exclude tropospheric ozone and carbon monoxide  
- GMST: 1980-2030 linear 1°C and 1.5°C increase (lower- and upper-range, respectively; page 440\)

63) Ciborowski 1989,[112](https://www.zotero.org/google-docs/?crHz25) summarized in Badr 1991[113](https://www.zotero.org/google-docs/?yb9EP8)  
1. excluding tropospheric ozone, ozone depletion, stratospheric water vapor, and “*other*” implies 1.10°C to 3.57°C for 1985-2035 (figure 14.2 on page 223 of Ciborowski 1989\)  
2. “*three or four decades*” changes the time frame from 1985-2035 to 1985-2065 and 1985-2075 (page 222\)  
3. lower-range: 1.10°C for 1985-2075 implies 0.61°C for 1985-2035   
4. upper-range: 3.57°C for 1985-2065 implies 2.23°C for 1985-2035  
5. 1985 values of 345.5 ppm for CO2, 305.3ppb N2O, 1657.2ppb CH4, 383.6ppt CFC-12, 212.9ppt CFC-11, and 40ppt CFC-113 (page 215; NOAA 2025[114](https://www.zotero.org/google-docs/?RYb7iY))  
6. 107.3ppt to 1230ppt HCFC-22 increase for 1985-2035, increasing at 5%/year (figure 14.2)  
- greenhouse gas increases:  
- lower-range: 1985-2035 increases from 345.5 to 450 ppm for CO2, 305.3 to 375ppb N2O, 1657.2 to 2950ppb CH4, 383.6 to 1200ppt CFC-12, 212.9 to 700ppt of CFC-11, 40 to 190ppt CFC-113, and 107.3 to 1230ppt HCFC-22; exclude tropospheric ozone, ozone depletion, stratospheric water vapor, and “*other*” (figure 14.2 and page 215; NOAA 2025[114](https://www.zotero.org/google-docs/?UB25Ln))  
- higher-range: 1985-2035 increases from 345.5 to 450 ppm for CO2, 305.3 to 375ppb N2O, 1657.2 to 2950ppb CH4, 383.6 to 1600ppt CFC-12, 212.9 to 1000ppt of CFC-11, 40 to 190ppt CFC-113, and 107.3 to 1230ppt HCFC-22; exclude tropospheric ozone, ozone depletion, stratospheric water vapor, and “*other*” (figure 14.2 and page 215; NOAA 2025[114](https://www.zotero.org/google-docs/?kWVxEY))  
- forcing: for lower- and upper-range linearly interpolate between the 1985 and 2035 concentration for each greenhouse gas, except HCFC-22 for which annual forcing values are calculated based on a 5%/year increase in concentration   
- GMST: 1985-2035 linear interpolation from forcing for 0.61°C and 2.23°C (lower- and upper-range, respectively)  
    
64) Harvey 1989[115](https://www.zotero.org/google-docs/?0a7LoD)  
- forcing: 1989-2024 annual values from figure 6b for the “*Total*” and “*\+1% to 2020*” line  
- GMST: 1989-2024 annual values from figure 6a for the “*ΔT2X \= 2.0°C*” and “*\+1% to 2020*” line

65) Budyko 1990[116](https://www.zotero.org/google-docs/?TFGwk9)  
1. 100% CO2 increase implies ‘2.1°C / 3.71 Wm\-2’ (page 11\)  
2. 380 ppm to 590 ppm CO2\-equivalents increase for 1980-2030 (page 11 of Budyko 1990, citing page 189 of Bolin 1986[117](https://www.zotero.org/google-docs/?B8bJy7))  
3. 380 ppm to 590 ppm CO2 increase for 1980-2030 implies 2.35 Wm\-2  
4. 2.35 Wm\-2 linear increase for 1980-2030 implies 2.07 Wm\-2 for 1980-2024  
5. 2.07 Wm\-2 multiplied by ‘2.1°C / 3.71 Wm\-2’ implies 1.2°C for 1980-2024 (1.2°C corresponds well with table 1 of Budyko 1990, as required by the following from page 11: “*This value corresponds sufficiently well with the data presented in Table 1*”)  
- forcing: 1980-2030 annual values for a 380 ppm to 590 ppm CO2\-equivalents increase   
- GMST: 1980-2000 annual values from figure 2 for line “*3*”, extrapolated for 2000-2024 such that \~1.2°C warming occurs for 1980-2024 

66) Etkin 1990[118](https://www.zotero.org/google-docs/?XoqRek)  
- greenhouse gases: 1990-2024 annual values from figure 8 for “*LB'*” and “*UB'*” (lower- and upper-range, respectively)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1990-2024 annual values from figure 9 for “*low scenario*” and “*upper scenario*” (lower- and upper-range, respectively)

67) IPCC 1990[119](https://www.zotero.org/google-docs/?iqJZUj)  
- forcing: 1990-2024 for “*SCENARIO BaU*” in figure 2.4  
- GMST: 1990-2024 for “*LOW*”, “*BEST*”, and “*HIGH*” lines in figure 8 (lower-range, average, and upper-range, respectively)  
    
68) Mitchell 1990[120](https://www.zotero.org/google-docs/?7kN2qh)  
- forcing: 1989-2035 linear 3.5 Wm\-2 increase (page 27\)  
- GMST: 1989-2035 for line ‘*b*’ in the figure on page 27

69) Rotmans 1990[121](https://www.zotero.org/google-docs/?XGKdjN)  
- greenhouse gases: 1990-2024 annual values for “*L C Risk*” from figure 3   
- forcing: calculated from annual greenhouse gas values  
- GMST: 1990-2024 annual values for dashed lines from figure 2 (lower- and upper-range)

70) Wang 1990[122](https://www.zotero.org/google-docs/?Ho3DhF)  
- greenhouse gases: 1985-2024 CO2 and non-CO2 annual values using 1985 and 2060 values in table 2, with annual increases of 0.54% for CO2, 1.003% for CH4, 0.251% for N2O, 1.54% for CFC-11, and 1.70% for CFC-12 (page 154\)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1985-2060 linear interpolation from forcing for 1.1°C and 2.5°C (lower- and upper-range, respectively; table 3 and page 155\)  
    
71) Warrick 1990[123](https://www.zotero.org/google-docs/?srrSYN)  
- greenhouse gases: 1990-2024 annual values from figure 1 for “*low*” and “*high*” (lower-range and higher-range, respectively)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1990-2024 annual values from figure 3 for “*low*” and “*high*” (lower-range and higher-range, respectively)  
    
72) Jastrow 1991[124](https://www.zotero.org/google-docs/?UsBgLB)  
- forcing: 1991-2024 from figure 2.4 of IPCC 1990[119](https://www.zotero.org/google-docs/?TY3o1y) for “*BaU*” (page 1341 of Jastrow 1991\)  
- GMST: 1991-2050 linear interpolation from forcing for 0.4°C, 1.1°C, and 1.8°C (lower-range, average, and upper-range, respectively; page 1343\)  
    
73) Bongaarts 1992[125](https://www.zotero.org/google-docs/?EQU6HD)  
- greenhouse gases: 1992-2024 annual values from figure 4 for “*no response scenario*”  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1992-2024 annual values from figure 4 for “*no response scenario*”  
    
74) Cubasch 1992[126](https://www.zotero.org/google-docs/?4TuJCm)  
- forcing: 1992-2024 from figure 2.4 of IPCC 1990[119](https://www.zotero.org/google-docs/?Snzzop) for “*BaU*” (figures 10 and 11 of Cubasch 1992\)  
- GMST: 1992-2024 for the “*CORR. A*” line from figure 11 of Cubasch 1992   
    
75) Hoffert 1992[127](https://www.zotero.org/google-docs/?mpWobK)  
1. 2.3 ± 0.9°C equilibrium climate sensitivity from Hoffert 1992 is less than 2.5°C from IPCC 1990[119](https://www.zotero.org/google-docs/?L5mb0H) , implying Hoffert 1992 projects less warming than IPCC 1990 for the same forcing (page 573 of Hoffert 1992; page xxv of IPCC 1990[119](https://www.zotero.org/google-docs/?7uuL6P))  
2. \~4.0°C of 1900-2100 warming from IPCC 1990 should therefore exceed warming from Hoffert 1992, implying “*3-4 °C*” from Hoffert 1992 is the lower- and upper-range for 1900-2100 (page 576 of Hoffert 1992; figure 9 of IPCC 1990\)  
3. 9.39 Wm\-2 of forcing for 1900-2100 and 2.04 Wm\-2 for 1992-2024 (figure 6 of IPCC 1990; page 576 of Hoffert 1992\)  
4. lower-range: ‘3°C / 9.39 Wm\-2’ multiplied by 2.04 Wm\-2 implies 0.65°C of 1992-2024 warming   
5. upper-range: ‘4°C / 9.39 Wm\-2’ multiplied by 2.04 Wm\-2 implies 0.87°C of 1992-2024 warming  
- forcing: 1992-2024 from figure 2.4 of IPCC 1990[119](https://www.zotero.org/google-docs/?a5Vyns) for “*BaU*”  
- GMST: 1992-2024 linear interpolation from forcing for 0.65°C and 0.87°C (lower- and upper-range, respectively)  
    
76) IPCC 1992[128](https://www.zotero.org/google-docs/?ItBqm8)  
- forcing: 1990-2024 from figure 6 of IPCC 1995[129](https://www.zotero.org/google-docs/?o4NsVz) for “*IS92a*” (figure 2a caption of IPCC 1992\)  
- GMST: 1990-2024 from figure 2a of IPCC 1992 for “*Low*”, “*Best estimate*”, and “*High*” (lower-range, average, and upper-range, respectively)

77) Kim 1992[130](https://www.zotero.org/google-docs/?21T3Si)  
- forcing: 1992-2024 from figure 2.4 of IPCC 1990[119](https://www.zotero.org/google-docs/?mh7tX1) for “*BaU*” (page 10,076 of Kim 1992\)  
- GMST: 1992-2024 from figure 7 of Kim 1992  
    
78) Nordhaus 1992[131](https://www.zotero.org/google-docs/?btbcXA)  
- greenhouse gases: 1992-2024 annual values from figure 2 for “*uncontrolled path*”, multiplied by 0.471 to convert gigatons C to ppm CO2   
- forcing: calculated from annual greenhouse gas values  
- GMST: 1992-2024 annual values from figure 3 for “*no controls*”

79) Rao 1992[132](https://www.zotero.org/google-docs/?yXMgdu)  
1. “*CFC*” in figures 2 through 4 is the sum of CFC-11 and CFC-12 (tables 4 and 5\)  
2. CFC-11 and CFC-12 increases are of the same order of magnitude (NOAA 2025[114](https://www.zotero.org/google-docs/?wk7UlL))  
3. radiative efficiency in Wm\-2ppb\-1 is 0.26 for CFC-11 and is 0.32 for CFC-12, implying a value of 0.3 is reasonable for the average of CFC-11 and CFC-12 (table 8.A.1 of IPCC 2013[34](https://www.zotero.org/google-docs/?GxJzG1))  
- greenhouse gases: 1992-2024 annual values from figure 2  
- forcing: calculated from annual greenhouse gas values, assuming 0.3 Wm\-2ppb\-1 radiative efficiency for “*CFC*”  
- GMST: 1992-2024 annual values from figure 4 for “*CFC (N)*”, excluding “*CFC (MP-1987)*” and “*CFC (MP-1990)*”  
    
80) Roeckner 1992[133](https://www.zotero.org/google-docs/?3bXSTd)  
- forcing: 1992-2024 annual values for scenario “*BaU*” from figure A.6 of IPCC 1990[119](https://www.zotero.org/google-docs/?xcSF18) (figure 12 of Roeckner 1992\)  
- GMST: 1992-2024 annual values from figure 12 for “*SCENARIO A*” of “*ECHAM1+OPYC*”  
    
81) Wigley 1992[134](https://www.zotero.org/google-docs/?n09sNR)  
- forcing: 1992-2024 annual values from figure 4 for “*M*”  
- GMST: 1992-2024 annual values from figure 4 for the “*M*” solid line

82) Manabe 1993[135](https://www.zotero.org/google-docs/?HY9g6m)  
- greenhouse gases: 1992-2024 CO2 increase from 356 ppm, with 1992 being the “*present*” (“*4XC*” in figure 1a)  
- forcing: calculated from annual greenhouse gas values  
- GMST: 1992-2024 increase, with 1992 being the “*present*” (“*4XC*” in figure 1b)  
    
83) IPCC 1995[129](https://www.zotero.org/google-docs/?o7toqP)  
- forcing: 1995-2024 annual values from figure 6a for “*IS92c*”, “*IS92a*”, and “*IS92e*” (lower-range, average, and upper-range, respectively)  
- GMST: 1995-2024 annual values for “*Including changes* \[...\]” solid lines in figure 19 for “*IS92c/1.5*”, “*IS92a/2.5*”, and “*IS92e/4.5*” (lower-range, average, and upper-range, respectively)  
    
84) IPCC 2001[136](https://www.zotero.org/google-docs/?zqJNWs)  
- forcing: 2000-2024 linear interpolation between values in table II.3.11 on page 823 of appendix II for A2  
- GMST: 2000-2024 linear interpolation between values in table II.4 on page 824 of appendix II for A2 (average) and “*Model ensemble all SRES envelop*” on figure 9.14 on page 555 (lower-range and upper range)  
    
85) IPCC 2007[137](https://www.zotero.org/google-docs/?PJO30r)  
- forcing: A1B scenario for GISS model E (page 14 of the supporting information of Hausfather 2020[1](https://www.zotero.org/google-docs/?ihuY9I))  
- GMST: available runs for A1B scenario from KNMI Climate Explorer (page 14 of the supporting information of Hausfather 2020[1](https://www.zotero.org/google-docs/?uLxohs))

**H) References**

[1\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hausfather Z, Drake HF, Abbott T, Schmidt GA (2020) Evaluating the Performance of Past Climate Model Projections. Geophysical Research Letters 47:e2019GL085378](https://www.zotero.org/google-docs/?g3UqoE) 

[2\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Supran G, Rahmstorf S, Oreskes N (2023) Assessing ExxonMobil’s global warming projections. Science 379:eabk0063](https://www.zotero.org/google-docs/?g3UqoE) 

[3\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Intergovernmental Panel On Climate Change (IPCC) (2023) Climate Change 2021 – The Physical Science Basis: Working Group I Contribution to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change, 1st ed. https://doi.org/10.1017/9781009157896](https://www.zotero.org/google-docs/?g3UqoE) 

[4\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Frame DJ, Stone DA (2013) Assessment of the first consensus prediction on climate change. Nature Clim Change 3:357–359](https://www.zotero.org/google-docs/?g3UqoE) 

[5\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Lapenis A (2020) A 50-Year-Old Global Warming Forecast That Still Holds Up. Eos. https://doi.org/10.1029/2020EO151822](https://www.zotero.org/google-docs/?g3UqoE) 

[6\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Anderson TR, Hawkins E, Jones PD (2016) CO2, the greenhouse effect and global warming: from the pioneering work of Arrhenius and Callendar to today’s Earth System Models. Endeavour 40:178–187](https://www.zotero.org/google-docs/?g3UqoE) 

[7\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hawkins E (2026) Revisiting the near-term projection from IPCC AR5. Climate Lab Book](https://www.zotero.org/google-docs/?g3UqoE) 

[8\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Schmidt GA (2026) Model-Observation Comparisons. RealClimate](https://www.zotero.org/google-docs/?g3UqoE) 

[9\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Peterson TC, Connolley WM, Fleck J (2008) The myth of the 1970s global cooling scientific consensus. Bull Amer Meteor Soc 89:1325–1338](https://www.zotero.org/google-docs/?g3UqoE) 

[10\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Weart SR (2010) The idea of anthropogenic global climate change in the 20th century. WIREs Climate Change 1:67–81](https://www.zotero.org/google-docs/?g3UqoE) 

[11\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Shulman PA (2010) Linking energy and climate (before 1974). WIREs Climate Change 1:773–780](https://www.zotero.org/google-docs/?g3UqoE) 

[12\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Edwards PN (2011) History of climate modeling. WIREs Climate Change 2:128–139](https://www.zotero.org/google-docs/?g3UqoE) 

[13\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Knutti R, Rugenstein MAA, Hegerl GC (2017) Beyond equilibrium climate sensitivity. Nature Geosci 10:727–736](https://www.zotero.org/google-docs/?g3UqoE) 

[14\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Heymann M, Achermann D (2018) From Climatology to Climate Science in the Twentieth Century. In: White S, Pfister C, Mauelshagen F (eds) The Palgrave Handbook of Climate History. Palgrave Macmillan UK, London, pp 605–632](https://www.zotero.org/google-docs/?g3UqoE) 

[15\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Weart S (2025) The Carbon Dioxide Greenhouse Effect. In: The Discovery of Global Warming. https://history.aip.org/climate/co2.htm.](https://www.zotero.org/google-docs/?g3UqoE) 

[16\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Nuccitelli D (2011) Comparing Global Temperature Predictions. In: Skeptical Science. https://skepticalscience.com/comparing-global-temperature-predictions.html.](https://www.zotero.org/google-docs/?g3UqoE) 

[17\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Wigley TM (2020) How Good Are Past Predictions of Global Warming? Skeptical Inquirer 44:](https://www.zotero.org/google-docs/?g3UqoE) 

[18\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Watts A (2025) Failed Prediction Timeline. Watts Up With That?](https://www.zotero.org/google-docs/?g3UqoE) 

[19\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Ebell M, Milloy SJ (2019) Wrong Again: 50 Years of Failed Eco-pocalyptic Predictions. Competitive Enterprise Institute](https://www.zotero.org/google-docs/?g3UqoE) 

[20\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Perry MJ (2022) 18 Spectacularly Wrong Predictions Were Made Around the Time of the First Earth Day in 1970, Expect More This Year. American Enterprise Institute](https://www.zotero.org/google-docs/?g3UqoE) 

[21\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Goldman D (2020) Concerns surrounding “Evaluating the performance of past climate model projections.” https://doi.org/10.13140/RG.2.2.22390.34887](https://www.zotero.org/google-docs/?g3UqoE) 

[22\.](https://www.zotero.org/google-docs/?g3UqoE) 	[(1953) Science: Invisible Blanket. Time LXI:](https://www.zotero.org/google-docs/?g3UqoE) 

[23\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Kasprak A (2016) Did a 1912 Newspaper Article Predict Global Warming? In: Snopes. https://www.snopes.com/fact-check/1912-article-global-warming/.](https://www.zotero.org/google-docs/?g3UqoE) 

[24\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Eichhorn N (1963) Implications of Rising Carbon Dioxide Content of the Atmosphere: A Statement. 15](https://www.zotero.org/google-docs/?g3UqoE) 

[25\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Ekholm N (1901) ON THE VARIATIONS OF THE CLIMATE OF THE GEOLOGICAL AND HISTORICAL PAST AND THEIR CAUSES. Quart J Royal Meteoro Soc 27:1–62](https://www.zotero.org/google-docs/?g3UqoE) 

[26\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Callendar GS (1949) Can Carbon Dioxide Influence Climate? Weather 4:310–314](https://www.zotero.org/google-docs/?g3UqoE) 

[27\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Gebhart R (1967) On the significance of the shortwave CO2-absorption in investigations concerning the CO2-theory of climatic change. Arch Met Geoph Biokl B 15:52–61](https://www.zotero.org/google-docs/?g3UqoE) 

[28\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Flohn H (1941) Die Tätigkeiten des Menschen als Klimafaktor. Zeitschrift für Erdkunde 9:13–22](https://www.zotero.org/google-docs/?g3UqoE) 

[29\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Budyko M, Vinnikov K (1976) The global warming. Meteorol Hidrol 16–26](https://www.zotero.org/google-docs/?g3UqoE) 

[30\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Environmental Pollution Panel, United States President’s Science Advisory Committee (1965) Restoring the quality of our environment. The White House](https://www.zotero.org/google-docs/?g3UqoE) 

[31\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Schneider SH, Thompson SL (1981) Atmospheric CO2 and climate: Importance of the transient response. J Geophys Res 86:3135–3147](https://www.zotero.org/google-docs/?g3UqoE) 

[32\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hansen J, Fung I, Lacis A, Rind D, Lebedeff S, Ruedy R, Russell G, Stone P (1988) Global climate changes as forecast by Goddard Institute for Space Studies three‐dimensional model. J Geophys Res 93:9341–9364](https://www.zotero.org/google-docs/?g3UqoE) 

[33\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Rohatgi A (2024) WebPlotDigitizer 4.8. In: automeris.io. https://apps.automeris.io/wpd4/.](https://www.zotero.org/google-docs/?g3UqoE) 

[34\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Intergovernmental Panel On Climate Change (ed) (2014) Climate Change 2013 – The Physical Science Basis: Working Group I Contribution to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change, 1st ed. https://doi.org/10.1017/CBO9781107415324](https://www.zotero.org/google-docs/?g3UqoE) 

[35\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Mitchell JM (1961) Recent secular changes of global temperature. Annals of the New York Academy of Sciences 95:235–250](https://www.zotero.org/google-docs/?g3UqoE) 

[36\.](https://www.zotero.org/google-docs/?g3UqoE) 	[MacDonald GJF (1966) Weather and climate modification—problems and prospects. Bulletin of the American Meteorological Society 47:4–20](https://www.zotero.org/google-docs/?g3UqoE) 

[37\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Malone TF (1967) Weather Modification: Implications of the New Horizons in Research. Science 156:897–901](https://www.zotero.org/google-docs/?g3UqoE) 

[38\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Ohring G (1967) Radiative transfer and the thermal structure of planetary atmospheres. Survey Symposium on Radiation](https://www.zotero.org/google-docs/?g3UqoE) 

[39\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Sherwood SC, Webb MJ, Annan JD, et al (2020) An Assessment of Earth’s Climate Sensitivity Using Multiple Lines of Evidence. Reviews of Geophysics 58:e2019RG000678](https://www.zotero.org/google-docs/?g3UqoE) 

[40\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Haustein K, Otto FEL, Venema V, Jacobs P, Cowtan K, Hausfather Z, Way RG, White B, Subramanian A, Schurer AP (2019) A Limited Role for Unforced Internal Variability in Twentieth-Century Warming. Journal of Climate 32:4893–4917](https://www.zotero.org/google-docs/?g3UqoE) 

[41\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Raghuraman SP, Paynter D, Ramaswamy V, Menzel R, Huang X (2023) Greenhouse Gas Forcing and Climate Feedback Signatures Identified in Hyperspectral Infrared Satellite Observations. Geophysical Research Letters 50:e2023GL103947](https://www.zotero.org/google-docs/?g3UqoE) 

[42\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Meehl GA, Senior CA, Eyring V, Flato G, Lamarque J-F, Stouffer RJ, Taylor KE, Schlund M (2020) Context for interpreting equilibrium climate sensitivity and transient climate response from the CMIP6 Earth system models. Sci Adv 6:eaba1981](https://www.zotero.org/google-docs/?g3UqoE) 

[43\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hausfather Z, Marvel K, Schmidt GA, Nielsen-Gammon JW, Zelinka M (2022) Climate simulations: recognize the ‘hot model’ problem. Nature 605:26–29](https://www.zotero.org/google-docs/?g3UqoE) 

[44\.](https://www.zotero.org/google-docs/?g3UqoE) 	[McKitrick R (2020) Explaining the Discrepancies Between Hausfather et al. (2019) and Lewis\&Curry (2018). Climate Etc.](https://www.zotero.org/google-docs/?g3UqoE) 

[45\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Arrhenius S (1896) Naturens värmehushållning. Nordisk tidskrift 14:121–130](https://www.zotero.org/google-docs/?g3UqoE) 

[46\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Henning Rodhe, Robert Charlson, Elisabeth Crawford (1997) Svante Arrhenius and the greenhouse effect. Ambio 26:2–5](https://www.zotero.org/google-docs/?g3UqoE) 

[47\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Callendar GS (1938) The artificial production of carbon dioxide and its influence on temperature. Quart J Royal Meteoro Soc 64:223–240](https://www.zotero.org/google-docs/?g3UqoE) 

[48\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Plass GN (1953) The Carbon Dioxide Theory of Climatic Change. In: Proceedings of the 122nd National Meeting, American Meteorological Society, Washington, D. C., April 29-May 4, 1953\. Washington, DC, p 80](https://www.zotero.org/google-docs/?g3UqoE) 

[49\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Northcott R (1953) The Earth is Warming Up. Journal of the Royal Astronomical Society of Canada 47:260](https://www.zotero.org/google-docs/?g3UqoE) 

[50\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hewson EW (1953) Atmospheric pollution in relation to microclimatology and micrometeorology: some problems. Proceedings of the Toronto Meteorological Conference](https://www.zotero.org/google-docs/?g3UqoE) 

[51\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Plass GN (1956) The Carbon Dioxide Theory of Climatic Change. Tellus 8:140–154](https://www.zotero.org/google-docs/?g3UqoE) 

[52\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Plass GN (1959) Carbon Dioxide and Climate. Scientific American 201:41–47](https://www.zotero.org/google-docs/?g3UqoE) 

[53\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hepting GH (1963) Climate and Forest Diseases. Annu Rev Phytopathol 1:31–50](https://www.zotero.org/google-docs/?g3UqoE) 

[54\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Kondratiev KY, Niilisk HI (1960) On the question of carbon dioxide heat radiation in the atmosphere. Geofisica Pura e Applicata 46:216–230](https://www.zotero.org/google-docs/?g3UqoE) 

[55\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Wilkins EM (1961) Seasonal variations in atmospheric carbon dioxide concentration. J Geophys Res 66:1314–1315](https://www.zotero.org/google-docs/?g3UqoE) 

[56\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Sargent, F (1967) Adaptive Strategy for Air Pollution. BioScience 17:691–697](https://www.zotero.org/google-docs/?g3UqoE) 

[57\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Fletcher JO (1969) Controlling the planet’s climate. Impact of science on society 19:151–168](https://www.zotero.org/google-docs/?g3UqoE) 

[58\.](https://www.zotero.org/google-docs/?g3UqoE) 	[The Weather Modification Research Project of the RAND Corporation (1969) Weather-modification progress and the need for interactive research. Bulletin of the American Meteorological Society 50:216–247](https://www.zotero.org/google-docs/?g3UqoE) 

[59\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Peterson EK (1969) Carbon dioxide affects global ecology. Environ Sci Technol 3:1162–1169](https://www.zotero.org/google-docs/?g3UqoE) 

[60\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Tilson S (1969) Electricity and weather modification III. Pollution problems and social impact. IEEE Spectr 6:52–61](https://www.zotero.org/google-docs/?g3UqoE) 

[61\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Austin AL, Brewer JW (1970) World population growth and related technical problems. IEEE Spectr 7:43–54](https://www.zotero.org/google-docs/?g3UqoE) 

[62\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Barrett EW, Pueschel RF, Weickmann HK, Kuhn PM (1970) Inadvertent Modification of Weather and Climate by Atmospheric Pollutants. Atmospheric Physics & Chemistry Laboratory](https://www.zotero.org/google-docs/?g3UqoE) 

[63\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Benton GS (1970) Carbon dioxide and its role in climate change. Proc Natl Acad Sci USA 67:898–899](https://www.zotero.org/google-docs/?g3UqoE) 

[64\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Fletcher JO (1970) Polar Ice and the Global Climate Machine. Bulletin of the Atomic Scientists 26:40–47](https://www.zotero.org/google-docs/?g3UqoE) 

[65\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Landsberg HE (1970) Man-Made Climatic Changes: Man’s activities have altered the climate of urbanized areas and may affect global climate in the future. Science 170:1265–1274](https://www.zotero.org/google-docs/?g3UqoE) 

[66\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Manabe S (1970) The Dependence of Atmospheric Temperature on the Concentration of Carbon Dioxide. In: Singer SF (ed) Global Effects of Environmental Pollution. Springer Netherlands, Dordrecht, pp 25–29](https://www.zotero.org/google-docs/?g3UqoE) 

[67\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Mitchell JM (1970) A Preliminary Evaluation of Atmospheric Pollution as a Cause of the Global Temperature Fluctuation of the Past Century. In: Singer SF (ed) Global Effects of Environmental Pollution. Springer Netherlands, Dordrecht, pp 139–155](https://www.zotero.org/google-docs/?g3UqoE) 

[68\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Presidential Council on Environmental Quality (1970) Man’s inadvertent modification of weather and climate. Bulletin of the American Meteorological Society 51:1043–1047](https://www.zotero.org/google-docs/?g3UqoE) 

[69\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Lovelock JE (1971) Air pollution and climatic change. Atmospheric Environment (1967) 5:403–411](https://www.zotero.org/google-docs/?g3UqoE) 

[70\.](https://www.zotero.org/google-docs/?g3UqoE) 	[MacDonald GJF (ed) (1971) Climatic consequences of increased carbon dioxide in the atmosphere. Power Generation and Environmental Change. https://doi.org/10.7551/mitpress/5495.001.0001](https://www.zotero.org/google-docs/?g3UqoE) 

[71\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Matthews WH (1971) Inadvertent climate modification: Report of the study of man’s impact on climate (SMIC). Study of Man’s Impact on Climate](https://www.zotero.org/google-docs/?g3UqoE) 

[72\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Matthews WH (1973) Climatic effects of man’s activities. International Journal of Environmental Studies 4:283–289](https://www.zotero.org/google-docs/?g3UqoE) 

[73\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Rasool SI, Schneider SH (1971) Atmospheric Carbon Dioxide and Aerosols: Effects of Large Increases on Global Climate. Science 173:138–141](https://www.zotero.org/google-docs/?g3UqoE) 

[74\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Budyko MI (1972) The future climate. EoS Transactions 53:868–874](https://www.zotero.org/google-docs/?g3UqoE) 

[75\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Budyko MI (1972) Vliyaniye cheloveka na klimat. Gidrometeoizdat](https://www.zotero.org/google-docs/?g3UqoE) 

[76\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Ferland RE, Howell JR (1972) Water Vapor, CO2 and Particulate Effects on the Atmospheric Temperature Profile. Proceedings of the 1972 Heat Transfer and Fluid Mechanics Institute](https://www.zotero.org/google-docs/?g3UqoE) 

[77\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Sawyer JS (1972) Man-made Carbon Dioxide and the “Greenhouse” Effect. Nature 239:23–26](https://www.zotero.org/google-docs/?g3UqoE) 

[78\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Machta L (1972) Mauna Loa and global trends in air quality. Bull Amer Meteor Soc 53:402–420](https://www.zotero.org/google-docs/?g3UqoE) 

[79\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Machta L (1972) Prediction of CO2 in the atmosphere. In: Proceedings of the 24th Brookhaven Symposium in Biology. Upton, New York, pp 21–31](https://www.zotero.org/google-docs/?g3UqoE) 

[80\.](https://www.zotero.org/google-docs/?g3UqoE) 	[National Science Board (1972) Patterns and Perspectives in Environmental Science. National Science Foundation](https://www.zotero.org/google-docs/?g3UqoE) 

[81\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Palmer BJ (1973) A Review Paper on the Effect of Carbon Dioxide and Aerosols on Climate Modification. Environmental Letters 5:249–265](https://www.zotero.org/google-docs/?g3UqoE) 

[82\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Landsberg H, Machta L (1974) Anthropogenic Pollution of the Atmosphere: Whereto? Ambio 3:146–150](https://www.zotero.org/google-docs/?g3UqoE) 

[83\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Barrett EW, Landsberg HE (1975) Inadvertent weather and climate modification. C R C Critical Reviews in Environmental Control 6:15–90](https://www.zotero.org/google-docs/?g3UqoE) 

[84\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Broecker WS (1975) Climatic Change: Are We on the Brink of a Pronounced Global Warming? Science 189:460–463](https://www.zotero.org/google-docs/?g3UqoE) 

[85\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Schneider SH, Dennett RD (1975) Climatic Barriers to Long-Term Energy Growth. Ambio 4:65–74](https://www.zotero.org/google-docs/?g3UqoE) 

[86\.](https://www.zotero.org/google-docs/?g3UqoE) 	[United States Committee for the Global Atmospheric Research Program (1975) Understanding climatic change: A program for action. National Academy of Sciences](https://www.zotero.org/google-docs/?g3UqoE) 

[87\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Watts RG, Hrubecky HF (1975) On the limits to energy growth. Technological Forecasting and Social Change 7:371–378](https://www.zotero.org/google-docs/?g3UqoE) 

[88\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Rotty RM, Weinberg AM (1977) How long is coal’s future? Climatic Change 1:45–57](https://www.zotero.org/google-docs/?g3UqoE) 

[89\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Budyko MI (1977) On present-day climatic changes. Tellus 29:193–204](https://www.zotero.org/google-docs/?g3UqoE) 

[90\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Nordhaus WD (1977) Strategies for the control of carbon dioxide. Cowles Foundation for Research in Economics](https://www.zotero.org/google-docs/?g3UqoE) 

[91\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Nordhaus WD (1977) Economic growth and climate: the carbon dioxide problem. The American Economic Review 67:341–346](https://www.zotero.org/google-docs/?g3UqoE) 

[92\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Kellogg WW, Schneider SH (1978) Global Air Pollution and Climate Change. IEEE Trans Geosci Electron 16:44–50](https://www.zotero.org/google-docs/?g3UqoE) 

[93\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Rotty RM (1978) Atmospheric carbon dioxide. Resources and Energy 1:231–249](https://www.zotero.org/google-docs/?g3UqoE) 

[94\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hoyt DV (1979) An empirical determination of the heating of the Earth by the carbon dioxide greenhouse effect. Nature 282:388–390](https://www.zotero.org/google-docs/?g3UqoE) 

[95\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Niehaus F, Williams J (1979) Studies of different energy strategies in terms of their effects on the atmospheric CO2 concentration. J Geophys Res 84:3123–3129](https://www.zotero.org/google-docs/?g3UqoE) 

[96\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hoffert MI, Callegari AJ, Hsieh C (1980) The role of deep sea heat storage in the secular response to climatic forcing. J Geophys Res 85:6667–6679](https://www.zotero.org/google-docs/?g3UqoE) 

[97\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Cess RD, Goldenberg SD (1981) The effect of ocean heat capacity upon global warming due to increasing atmospheric carbon dioxide. J Geophys Res 86:498–502](https://www.zotero.org/google-docs/?g3UqoE) 

[98\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hansen J, Johnson D, Lacis A, Lebedeff S, Lee P, Rind D, Russell G (1981) Climate Impact of Increasing Atmospheric Carbon Dioxide. Science 213:957–966](https://www.zotero.org/google-docs/?g3UqoE) 

[99\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Gilliland RL (1982) Solar, volcanic, and CO2 forcing of recent climatic changes. Climatic Change 4:111–131](https://www.zotero.org/google-docs/?g3UqoE) 

[100\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Seidel S, Keyes DL (1983) Can we delay a greenhouse warming?: The effectiveness and feasibility of options to slow a build-up of carbon dioxide in the atmosphere. Strategic Studies Staff, Office of Policy Analysis, Office of Policy and Resources Management](https://www.zotero.org/google-docs/?g3UqoE) 

[101\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hansen J, Lacis A, Rind D, Russell G, Stone P, Fung I, Ruedy R, Lerner J (1984) Climate sensitivity: Analysis of feedback mechanisms. In: Hansen JE, Takahashi T (eds) Geophysical Monograph Series. American Geophysical Union, Washington, D. C., pp 130–163](https://www.zotero.org/google-docs/?g3UqoE) 

[102\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Bach W (1985) Modeling the transient and equilibrium climate response to greenhouse gases. Annual Review in Automatic Programming 12:40–49](https://www.zotero.org/google-docs/?g3UqoE) 

[103\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hoffert MI, Flannery BP (1985) Model projections of the time-dependent response to increasing carbon dioxide. In: Projecting the climatic effects of increasing carbon dioxide. United States Department of Energy, pp 149–190](https://www.zotero.org/google-docs/?g3UqoE) 

[104\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Dickinson RE, Cicerone RJ (1986) Future global warming from atmospheric trace gases. Nature 319:109–115](https://www.zotero.org/google-docs/?g3UqoE) 

[105\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Jones PD, Wigley TML, Raper SCB (1987) The Rapidity of CO2-Induced Climatic Change: Observations, Model Results and Palaeoclimatic Implications. In: Berger WH, Labeyrie LD (eds) Abrupt Climatic Change. Springer Netherlands, Dordrecht, pp 47–55](https://www.zotero.org/google-docs/?g3UqoE) 

[106\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Peng L, Chou M, Arking A (1987) Climate warming due to increasing atmospheric CO2 : Simulations With a multilayer coupled atmosphere‐ocean seasonal energy balance model. J Geophys Res 92:5505–5521](https://www.zotero.org/google-docs/?g3UqoE) 

[107\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Ramanathan V, Callis L, Cess R, et al (1987) Climate‐chemical interactions and effects of changing atmospheric trace gases. Reviews of Geophysics 25:1441–1482](https://www.zotero.org/google-docs/?g3UqoE) 

[108\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Ramanathan V (1989) Observed increases in greenhouse gases and predicted climatic changes. In: The challenge of global warming. Island Press, Washington D. C., pp 239–247](https://www.zotero.org/google-docs/?g3UqoE) 

[109\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Tricot C, Berger A (1987) Modelling the equilibrium and transient responses of global temperature to past and future trace gas concentrations. Climate Dynamics 2:39–61](https://www.zotero.org/google-docs/?g3UqoE) 

[110\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Wigley TML, Raper SCB (1987) Thermal expansion of sea water associated with global warming. Nature 330:127–131](https://www.zotero.org/google-docs/?g3UqoE) 

[111\.](https://www.zotero.org/google-docs/?g3UqoE) 	[MacDonald GJ (1988) Scientific Basis for the Greenhouse Effect. Journal of Policy Analysis and Management 7:425](https://www.zotero.org/google-docs/?g3UqoE) 

[112\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Ciborowski P (1989) Sources, Sinks, Trends, and Opprtunities. In: The challenge of global warming. Island Press, Washington D. C., pp 213–230](https://www.zotero.org/google-docs/?g3UqoE) 

[113\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Badr O, Probert SD, O’Callaghan PW (1991) Atmospheric methane: Its contribution to global warming. Applied Energy 40:273–313](https://www.zotero.org/google-docs/?g3UqoE) 

[114\.](https://www.zotero.org/google-docs/?g3UqoE) 	[NOAA Global Monitoring Laboratory (2025) Annual Greenhouse Gas Index (AGGI). In: Global Monitoring Laboratory. https://gml.noaa.gov/aggi/aggi.html.](https://www.zotero.org/google-docs/?g3UqoE) 

[115\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Harvey LDD (1989) Managing atmospheric CO2. Climatic Change. https://doi.org/10.1007/BF00240464](https://www.zotero.org/google-docs/?g3UqoE) 

[116\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Budyko MI, Yefimova NA, Lokshina IYu (1990) Anticipated human modifications of global climate. Soviet Geography 31:11–23](https://www.zotero.org/google-docs/?g3UqoE) 

[117\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Bolle HJ, Seilerf W, Bolin B (1986) Assessing Their Role for Atmospheric Radiative Transfer. The greenhouse effect, climatic change and ecosystems](https://www.zotero.org/google-docs/?g3UqoE) 

[118\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Etkin D (1990) Greenhouse Warming: Consequences for Arctic Climate. J Cold Reg Eng 4:54–66](https://www.zotero.org/google-docs/?g3UqoE) 

[119\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Intergovernmental Panel On Climate Change (IPCC) (1990) Climate Change: The IPCC Scientific Assessment (1990). Cambridge University Press](https://www.zotero.org/google-docs/?g3UqoE) 

[120\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Mitchell J (1990) Greenhouse physics. Phys World 3:27–32](https://www.zotero.org/google-docs/?g3UqoE) 

[121\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Rotmans J, Swart R (1990) The gloomy greenhouse: Should the world phase out fossil fuels? Environmental Management 14:291–296](https://www.zotero.org/google-docs/?g3UqoE) 

[122\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Wang W-C, Molnar G, Ko MKW, Goldenberg S, Sze ND (1990) Atmospheric trace gases and global climate: a seasonal model study: ATMOSPHERIC TRACE GASES AND GLOBAL CLIMATE: A SEASONAL MODEL STUDY. Tellus B 42:149–161](https://www.zotero.org/google-docs/?g3UqoE) 

[123\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Warrick R, Farmer G (1990) The Greenhouse Effect, Climatic Change and Rising Sea Level: Implications for Development. Transactions of the Institute of British Geographers 15:5](https://www.zotero.org/google-docs/?g3UqoE) 

[124\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Jastrow R, Nierenberg W, Seitz F (1991) Global warming: What does the science tell us? Energy 16:1331–1345](https://www.zotero.org/google-docs/?g3UqoE) 

[125\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Bongaarts J (1992) Population Growth and Global Warming. Population and Development Review 18:299](https://www.zotero.org/google-docs/?g3UqoE) 

[126\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Cubasch U, Hasselmann K, Höck H, Maier-Reimer E, Mikolajewicz U, Santer BD, Sausen R (1992) Time-dependent greenhouse warming computations with a coupled ocean-atmosphere model. Climate Dynamics 8:55–69](https://www.zotero.org/google-docs/?g3UqoE) 

[127\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Hoffert MI, Covey C (1992) Deriving global climate sensitivity from palaeoclimate reconstructions. Nature 360:573–576](https://www.zotero.org/google-docs/?g3UqoE) 

[128\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Intergovernmental Panel On Climate Change (IPCC) (1992) Climate Change 1992: The Supplementary Report to the IPCC Scientific Assessment. Cambridge University Press](https://www.zotero.org/google-docs/?g3UqoE) 

[129\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Intergovernmental Panel On Climate Change (IPCC) (1995) Climate Change 1995: The Science of Climate Change. Cambridge University Press](https://www.zotero.org/google-docs/?g3UqoE) 

[130\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Kim K, North GR, Huang J (1992) On the transient response of a simple coupled climate system. J Geophys Res 97:10069–10081](https://www.zotero.org/google-docs/?g3UqoE) 

[131\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Nordhaus WD (1992) An Optimal Transition Path for Controlling Greenhouse Gases. Science 258:1315–1319](https://www.zotero.org/google-docs/?g3UqoE) 

[132\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Rao UR, Chakravarty SC (1992) An evaluation of global warming and its impact. Current Science 62:469–478](https://www.zotero.org/google-docs/?g3UqoE) 

[133\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Roeckner E (1992) Past, Present and Future Levels of Greenhouse Gases in the Atmosphere and Model Projections of Related Climatic Changes. J Exp Bot 43:1097–1109](https://www.zotero.org/google-docs/?g3UqoE) 

[134\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Wigley TML, Raper SCB (1992) Implications for climate and sea level of revised IPCC emissions scenarios. Nature 357:293–300](https://www.zotero.org/google-docs/?g3UqoE) 

[135\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Manabe S, Stouffer RJ (1993) Century-scale effects of increased atmospheric C02 on the ocean–atmosphere system. Nature 364:215–218](https://www.zotero.org/google-docs/?g3UqoE) 

[136\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Intergovernmental Panel On Climate Change (IPCC) (2001) Climate Change 2001: The Scientific Basis. Cambridge University Press](https://www.zotero.org/google-docs/?g3UqoE) 

[137\.](https://www.zotero.org/google-docs/?g3UqoE) 	[Intergovernmental Panel On Climate Change (IPCC) (2007) Climate Change 2007: The Physical Scientific Basis. Cambridge University Press](https://www.zotero.org/google-docs/?g3UqoE) 