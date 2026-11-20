# Habotrappan – premium-redesign

Öppna `index.html` i en modern webbläsare. Bilder, typsnitt, stilar och funktioner ingår. Ingen installation behövs. `redigerbar.html` är samma webbplats med separata assets- och fonts-mappar; behåll dem bredvid filen. Alla vyer nås i navigationen. De gamla sidnamnen finns som omdirigeringar i paketet.

## Innehåll
Fotografisk fullskärmshero med stor typografi, originalets nio galleribilder med kategorier och sökning, bildvisare, tre kundgruppsvyer, arbetssätt, familjehistoria, Jan-porträtt, FAQ, kontakt och förfrågningsformulär. Mobilanpassning, färgtema, tangentbordsstöd och reducerad rörelse. Designed by Ekom länkar till ekom.se.

## Förfrågan
Kontakt-/offertformulären validerar uppgifter och sammanställer ett mejlutkast till jan.englof@telia.com. Besökaren granskar, bifogar bilder eller ritningar och skickar själv från sitt mejlprogram. Ingen server, automatisk sändning, beställning, mottagningsbekräftelse eller bokning finns. Kopieringsknapp finns som alternativ till mejllänken. Telefonnummer är frivilligt.

Formulärtext finns endast i den öppna sidan och behålls vid intern navigation; omladdning rensar den. Ingen lokal lagring, spårning, annonsering eller extern kartinbäddning. Integritetstexten måste anpassas om ett formulärsystem eller annan datalagring ansluts senare.

## Verkligt ursprung
Företagsuppgifter, kundanpassad trapptillverkning och familjehistorik kommer från habotrappan.se. Jan Englöf är tredje generationens trappsnickare enligt originalsidan.1927/1960 beskriver verksamhetens familjehistoria, inte registreringsår för den nuvarande enskilda firman. Det publika verksamhetsnamnet Habo Trappindustri används; ingen AB-form, personligt organisationsnummer eller privat bostadsadress publiceras. Telefonnummer, mejl och verkstadsadress är originalets aktuella kontaktuppgifter.

Alla nio originalgalleribilder behålls. Sex har uppgraderats till visuellt verifierade högupplösta versioner av exakt samma fotografi i företagets offentliga WordPress-bildarkiv. Inga nya vinklar har uppfunnits eller grupperats till kundprojekt. Neutral titel och kategori beskriver vad som syns; de är inte modellnamn, träslagsintyg eller produktdata. Inga kundnamn, platser, priser, garantier, montage-/leveranslöften eller recensioner har hittats på. Övriga hero-, detalj- och hantverksbilder kommer från samma företags publicerade sidor/bildarkiv och dokumenteras med sina faktiska källor.

Originallogotypen är en JPEG med vit bakgrund, inte en transparent fil. Den har bevarats byte för byte. CSS-blandning gör att den inte får en synlig vit platta över ljusa ytor; i mörkt tema används en vit monokrom visning. Originalets bokstäver och linjer har inte genererats om och ingen bildmaskning har ändrat filen. Källor, dimensioner, ursprungshashar och levererade filers SHA256 finns i bildkallor.json och research/assets.json.

## Redigera
Källor: qa/template.html, qa/site.css, qa/site.js, qa/content.json och research/media.json. Med Python3, BeautifulSoup och Node kan du bygga om genom `python3 qa/build.py` och kontrollera med `python3 qa/verify.py`. Hash-navigation används för att vyerna ska fungera i en fristående fil. Titlar och beskrivningar byts vid navigation; detta är ingen serverrenderad flersideslösning för sökmotorindexering.

Typsnitt: Manrope från Google Fonts. SIL Open Font License finns i fonts. Källadress och filhash finns i typsnitt.json.

## Kontroll
JavaScript, alla vyer och interna länkar, inbäddade bilder/typsnitt, företagsuppgifter, Ekom-länk, metadata, ZIP CRC och exakt filinnehåll kontrolleras. Faktisk dator-/mobilgranskning och interaktionstest sker i lokal webbläsare. Mejllänkar provas utan sändning. Ingen mejlklient öppnas och inga meddelanden skickas till företaget. Native filöppning automatiseras inte. Webbplatsen är inte publicerad och ersätter inte företagets ordinarie webbplats.

### Utförda kontroller
12 vyer provade vid1440,1024,768,390 och320px, totalt60 faktiska webbläsarvisningar utan horisontellt överflöde, saknade vyer eller trasiga inlästa bilder. Heron kontrollerad i åtta format: full bredd, minst hela första skärmhöjden, läsbart innehåll och utrymme för mobilens kontaktfält. Korta skärmar får en naturligt högre hero. Galleri: kategori, sökning, tomt resultat, återställning, bildvisarens knappar/piltangenter/Escape och fokusåterställning testade. Mobilmeny, FAQ med tangentbord och mörkt/ljust tema testade. Kontakt/offert: förvald miljö, obligatoriska fält, frivillig telefon, felaktig mejl, sammanställning, tillbaka och kopiering testade. Inmatad HTML visas bokstavligt. Mejllänkens avkodade text matchar underlaget. Inga meddelanden skickades.
