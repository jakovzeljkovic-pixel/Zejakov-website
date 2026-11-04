"""English version of the site.

site.html stays the one source, written in Norwegian. build.py makes the
English pages from it by swapping whole pieces of text: a text node, an
attribute value or a quoted string in a script. A key only matches when it is
the entire piece, so short words like "Stue" never hit the middle of a sentence.

When the Norwegian copy changes, add or update the matching line here.
build.py lists every Norwegian piece it finds on the English pages that has
no translation yet, and every key here that no longer matches anything.
"""

# address of each English page (same slugs as build.PAGES)
PATHS = {
    "hjem": "/en/",
    "arbeid": "/en/work/",
    "heyerdahls": "/en/work/heyerdahls-vei-8b/",
    "tjenester": "/en/services/",
    "om": "/en/about/",
    "kontakt": "/en/contact/",
    "personvern": "/en/privacy/",
}

# slug -> (<title>, meta description)
META = {
    "hjem": ("Property film and photography in Oslo | ZEJAKOV MEDIA",
             "Media production for property in Oslo. Film, photography and drone footage "
             "for viewings and listings, all from one team. See the work and book a call."),
    "arbeid": ("Work: property film and photography from Oslo | ZEJAKOV MEDIA",
               "Homes we have photographed and filmed in and around Oslo. Each project "
               "includes film, photos and drone footage."),
    "heyerdahls": ("Heyerdahls vei 8 B: property film from Oslo | ZEJAKOV MEDIA",
                   "A detached house in Oslo overlooking the city. Film, photos and drone "
                   "footage from the same project, August 2026."),
    "tjenester": ("Property film, photography and drone in Oslo | ZEJAKOV MEDIA",
                  "A film in which the owner tells the story, photos with drone and evening light, "
                  "a 360 tour and architectural photography. Two packages for owners and agents in and around Oslo."),
    "om": ("Property photographer and filmmaker in Oslo | ZEJAKOV MEDIA",
           "Photography and film since 2023, now almost entirely homes. Based in Oslo, "
           "working worldwide."),
    "kontakt": ("Book a call about property film in Oslo | ZEJAKOV MEDIA",
                "Tell us about the home and we will set up a call. Property "
                "film, photography and drone in Oslo, and projects worldwide."),
    "personvern": ("Privacy | ZEJAKOV MEDIA",
                   "What we store and why. The site sets no cookies and has no tracking."),
}

# whole pieces of text, Norwegian -> English
T = {
    # head
    "Enebolig i Oslo filmet av ZEJAKOV MEDIA": "A detached house in Oslo filmed by ZEJAKOV MEDIA",
    "Medieproduksjon for eiendom i Oslo. Boligfilm, boligfoto og drone til visning og annonse, alt fra én leverandør. Se arbeidet og book befaring.":
        "Media production for property in Oslo. Film, photography and drone footage for viewings and listings, all from one team. See the work and book a call.",
    "Eiendomsfotograf": "Real estate photography",
    "Boligfoto": "Property photography",
    "Boligfilm": "Property film",
    "Dronefoto og dronefilm": "Drone photography and video",
    "Kveldsfoto": "Twilight photography",
    "Digital møblering": "Virtual staging",
    "Reels og video til sosiale medier": "Reels and video for social media",
    "Videografi for eiendom": "Real estate videography",
    "Medieproduksjon for eiendom": "Property media production",
    "Film av boligen til visning, annonse og sosiale medier.": "A film of the home for viewings, listings and social media.",
    "Stillbilder til annonsen.": "Stills for the listing.",
    "Foto og film fra luften av bolig og område.": "Aerial photos and film of the home and its surroundings.",
    "Bilder av boligen i kveldslys.": "Photos of the home in evening light.",
    "Tomme eller fulle rom møblert digitalt, merket som digitalt møblert.": "Empty or furnished rooms staged digitally, always labelled as virtually staged.",
    "Korte, stående videoer til sosiale medier.": "Short vertical videos for social media.",
    "Boligfilm av en enebolig i Oslo med utsikt over byen. Film, bilder og drone av ZEJAKOV MEDIA.":
        "Property film of a detached house in Oslo overlooking the city. Film, photos and drone footage by ZEJAKOV MEDIA.",

    # masthead, menu, footer
    "Hopp til innhold": "Skip to content",
    "Hjem": "Home",
    "Arbeid": "Work",
    "Tjenester": "Services",
    "Om oss": "About us",
    "Kontakt": "Contact",
    "Book befaring": "Book a call",
    "Meny": "Menu",
    "Lukk": "Close",
    "Bytt til lyst tema": "Switch to light mode",
    "Bytt til mørkt tema": "Switch to dark mode",
    "Språk": "Language",
    "ZEJAKOV ZELJKOVIC, org. 835 196 542": "ZEJAKOV ZELJKOVIC, org. no. 835 196 542",
    "Personvern": "Privacy",
    "Sosiale medier": "Social media",
    "Google-omtaler": "Google reviews",
    "Vi bruker opplysningene bare til å svare deg. Mer om dette på": "We only use your details to reply to you. More on the",
    "personvernsiden": "privacy page",
    "Ring 973 44 658": "Call 973 44 658",

    # home: hero
    "Hver bolig har en historie.": "Every home has a story.",
    "La oss fortelle den.": "Let's share it.",
    "Holder det med en vanlig annonse, er dette feil firma for deg.": "If a standard listing is all you need, we're not the right fit.",
    "Se arbeidet": "See the work",
    "Sett filmen på pause": "Pause the film",
    "Spill av filmen": "Play the film",

    # home: gallery
    "Siste oppdrag. Enebolig i Oslo,": "Latest project. A detached house in Oslo,",
    "foto og film i august 2026.": "photographed and filmed in August 2026.",
    "Bilder fra Heyerdahls vei 8 B": "Photos from Heyerdahls vei 8 B",
    "Forrige bilde": "Previous photo",
    "Neste bilde": "Next photo",
    "Se filmen": "Watch the film",
    "Fasaden mot hagen": "The façade facing the garden",
    "Eksteriør": "Exterior",
    "Interiør": "Interior",
    "Kjøkken og stue": "Kitchen and living room",
    "Fra luften": "From the air",
    "Stuebordet": "The coffee table",
    "Detalj": "Detail",

    # home: statement
    "Et hus til 35 millioner": "A $3.5 million home",
    "skal ikke se ut som et til 5.": "shouldn't look like a $500,000 one.",
    "Det er ikke mange kjøpere i den prisklassen, og de har allerede sett hundrevis av annonser med sjelløse rom og flatt lys. Vi lager bilder og film som forteller historien om boligen og viser hvordan det er å leve der. Det er det som får den til å skille seg ut.":
        "There aren't many buyers at that price, and they have already scrolled past hundreds of listings full of lifeless rooms and flat light. We make photos and film that tell the story of the home and show what it's like to live there. That is what makes it stand out.",

    # home: one house at a time
    "Ett hus om gangen.": "One house at a time.",
    "Mange meglerkjeder har faste fotoavtaler der det handler om å rekke flest mulig boliger hver dag. Fotografen har ofte rundt en time i hver bolig før det er videre til neste adresse. Det gir mange annonser, men sjelden en bolig som skiller seg ut.":
        "Many estate agency chains have fixed photography deals built around getting through as many homes as possible each day. The photographer often has about an hour in each home before moving on to the next address. You end up with plenty of listings, but rarely a home that stands out.",
    "Vi jobber motsatt. Vi tar bare et begrenset antall boliger i måneden, så hvert hus får den tiden og oppmerksomheten det fortjener. Vi venter på riktig lys, finner vinklene som viser hvordan det er å bo der, og redigerer hver bolig for seg.":
        "We work the other way round. We only take on a limited number of homes each month, so every house gets the time and attention it deserves. We wait for the right light, find the angles that show what it's like to live there, and edit every home individually.",
    "Få boliger i måneden": "A few homes a month",
    "Vi tar et begrenset antall oppdrag, så hvert hus får full oppmerksomhet.": "We take on a limited number of jobs, so every house gets our full attention.",
    "Ingen stoppeklokke": "No rush",
    "Vi blir til bildene sitter, uten en ny adresse som venter.": "We stay until the shots are right. There's no next address waiting.",
    "Samme folk hele veien": "The same people, start to finish",
    "De du snakker med, er de som fotograferer, filmer og redigerer.": "The people you talk to are the ones who shoot, film and edit.",

    # home: before / after
    "To versjoner av samme rom.": "Two versions of the same room.",
    "Til venstre: standard HDR, slik de fleste boligbilder ser ut. Flatt og jevnt lyst, der alt er like viktig. Det er ikke noe galt med det, men det blir fort borte blant alle de andre annonsene. Det vi lager, skiller seg ut.":
        "On the left: standard HDR, the way most property photos look. Flat and evenly lit, with everything given the same weight. There's nothing wrong with it, but it gets lost among all the other listings. What we make stands out.",
    "Soverom, Heyerdahls vei 8 B": "Bedroom, Heyerdahls vei 8 B",
    "Soverom i enebolig i Oslo, redigert av ZEJAKOV MEDIA": "Bedroom in a detached house in Oslo, edited by ZEJAKOV MEDIA",
    "Samme soverom med standard HDR": "The same bedroom with standard HDR",
    "Kjøkken og spisestue, samme bolig": "Kitchen and dining room, same home",
    "Kjøkken og spisestue i enebolig i Oslo, redigert av ZEJAKOV MEDIA": "Kitchen and dining room in a detached house in Oslo, edited by ZEJAKOV MEDIA",
    "Samme kjøkken og spisestue med standard HDR": "The same kitchen and dining room with standard HDR",
    "Dra i bildet": "Drag the image",
    "Til høyre er slik vi leverer. Hvert hus redigeres for seg, slik at farger, lys og stemning blir som når du står i rommet. Det gir et mer personlig og redaksjonelt uttrykk, og et riktigere bilde av boligen.":
        "On the right is what we deliver. Every house is edited on its own, so the colour, light and mood match what you see when you stand in the room. The result feels more personal and editorial, and gives a truer picture of the home.",
    "I boligfoto er det vanlig å fjerne alle fargestikk, så veggene blir helt hvite. For leiligheter og mindre boliger er det ofte riktig valg, og det leverer vi gjerne.":
        "In property photography it's common to remove every colour cast so the walls come out pure white. For flats and smaller homes that is often the right call, and we're happy to deliver it.",
    "I dyrere boliger er lys og materialer valgt med omhu. Det varme lyset fra lampene og det grønne fra hagen er en del av huset, og da er det en feil å vaske det bort. Gjort riktig er det nettopp det som gir bildet liv.":
        "In higher-end homes, the lighting and materials have been chosen with care. The warm glow of the lamps and the green from the garden are part of the house, so washing them out is a mistake. Done right, that is exactly what brings a photo to life.",

    # virtual staging (home and project)
    "Samme rom, flere muligheter.": "One room, many possibilities.",
    "Digital møblering. Tomme rom kan vi møblere digitalt. Fulle rom kan vi tømme på bildet og møblere på nytt, så kjøperen ser hva rommet kan brukes til. Selve rommet, med vegger, dører og vinduer, blir som det er. Eksempelet er aktivitetsrommet i kjelleren på Heyerdahls vei 8 B, tømt og møblert på fire måter.":
        "Virtual staging. We can furnish empty rooms digitally, and empty furnished rooms in the photo and restyle them, so buyers can see what a room could be used for. The room itself, with its walls, doors and windows, stays exactly as it is. The example is the basement activity room at Heyerdahls vei 8 B, emptied and furnished four different ways.",
    "Aktivitetsrommet, digitalt tømt": "The activity room, digitally emptied",
    "Aktivitetsrommet digitalt møblert som soverom, illustrasjon": "The activity room virtually staged as a bedroom, illustration",
    "Aktivitetsrommet digitalt møblert som stue, illustrasjon": "The activity room virtually staged as a living room, illustration",
    "Aktivitetsrommet digitalt møblert som kjøkken, illustrasjon": "The activity room virtually staged as a kitchen, illustration",
    "Aktivitetsrommet digitalt møblert som spillrom, illustrasjon": "The activity room virtually staged as a games room, illustration",
    "Digitalt tømt": "Digitally emptied",
    "Digitalt møblert": "Virtually staged",
    "Velg versjon av rommet": "Choose a version of the room",
    "Tomt": "Empty",
    "Soverom": "Bedroom",
    "Stue": "Living room",
    "Kjøkken": "Kitchen",
    "Spillrom": "Games room",
    "Det passer best når boligen står tom, når møblene tar oppmerksomheten fra rommet, eller når et rom som kjeller eller loft ikke har noen tydelig bruk. Det skal aldri skjule feil eller få boligen til å se bedre ut enn den er.":
        "It works best when the home is empty, when the furniture pulls attention away from the room, or when a space like a basement or loft has no obvious use. It should never hide flaws or make the home look better than it is.",
    "Aktivitetsrommet i kjelleren, tømt og møblert digitalt. De møblerte bildene er illustrasjoner av hvordan rommet kan brukes, ikke slik det står i dag.":
        "The basement activity room, emptied and furnished digitally. The staged images illustrate how the room could be used, not how it looks today.",

    # reviews
    "Hva kundene sier": "What clients say",
    "Forrige": "Previous",
    "Neste": "Next",
    "Legg igjen en vurdering": "Leave a review",
    "Skriv en omtale på Google": "Write a review on Google",
    "Navn": "Name",
    "Stjerner": "Stars",
    "1 stjerne": "1 star",
    "2 stjerner": "2 stars",
    "3 stjerner": "3 stars",
    "4 stjerner": "4 stars",
    "5 stjerner": "5 stars",
    "Din vurdering": "Your review",
    "Send inn": "Submit",
    "Takk. Vurderingen er mottatt og vises når den er godkjent.": "Thank you. Your review has been received and will appear once it's approved.",
    "Noe gikk galt. Prøv igjen senere.": "Something went wrong. Please try again later.",
    "Fyll inn navn, stjerner og tekst.": "Please add your name, a star rating and a few words.",

    # home: closing band
    "Terrassen på Heyerdahls vei 8 B i Oslo": "The terrace at Heyerdahls vei 8 B in Oslo",
    "Fortell oss om boligen, så tar vi det derfra.": "Tell us about the home, and we'll take it from there.",

    # work
    "Boliger vi har filmet.": "Homes we've filmed.",
    "Film og bilder fra oppdrag i Oslo og omegn.": "Film and photos from projects in and around Oslo.",
    "Heyerdahls vei 8 B: fasaden mot hagen": "Heyerdahls vei 8 B: the façade facing the garden",
    "Enebolig i Oslo med utsikt over byen. Film, bilder og drone fra samme oppdrag.": "A detached house in Oslo overlooking the city. Film, photos and drone footage, all from the same project.",

    # project page
    "Spill av filmen: Heyerdahls vei 8 B": "Play the film: Heyerdahls vei 8 B",
    "Huset ligger høyt og har utsikt over Oslo. Film, bilder, drone og klipp er gjort av oss.": "The house sits high above the city, with all of Oslo laid out below. We shot the film, the photos and the drone footage, and did the editing ourselves.",
    "Fasaden fra hjørnet": "The façade from the corner",
    "Terrassen": "The terrace",
    "Kjøkkenøya og stua": "The kitchen island and living room",
    "Hovedsoverom": "Main bedroom",
    "Barnerom": "Children's room",
    "Bad med badekar": "Bathroom with bathtub",
    "Aktivitetsrom": "Activity room",
    "Huset fra luften": "The house from the air",
    "Innkjørselen": "The driveway",
    "Kjøkken mot hagen": "Kitchen facing the garden",
    "Stue mot kjøkkenet": "Living room looking towards the kitchen",
    "Soverom, detalj": "Bedroom, detail",
    "Bad med dusj": "Bathroom with shower",
    "Detalj fra stua": "Detail from the living room",
    "Spisebord og kjøkken": "Dining table and kitchen",
    "Alle prosjekter": "All projects",
    "Vis større:": "View larger:",

    # services
    "Kjøperne i den prisklassen har sett hundrevis av annonser med de samme vinklene og det samme flate lyset. Ser en dyr bolig vanlig ut, begynner de å lure på hva de egentlig betaler for.":
        "Buyers in that price range have seen hundreds of listings with the same angles and the same flat light. When an expensive home looks ordinary, they start to wonder what they are really paying for.",
    "Vi lager en film der eieren forteller hvordan det var å bo der, sammen med bilder, drone og en 360-visning. Det gir kjøperen en grunn til å stole på boligen. Er du megler, har du noe konkret å tilby selgeren på befaringen.":
        "We make a film in which the owner tells what it was like to live there, together with photos, drone footage and a 360 tour. It gives buyers a reason to trust the home. If you're an agent, it gives you something concrete to offer the seller at the valuation meeting.",
    "Se pakkene":
        "See the packages",
    "Heyerdahls vei 8 B: fasaden mot hagen i kveldslys":
        "Heyerdahls vei 8 B: the façade facing the garden in evening light",
    "Et eksempel på Boligfortelling: Heyerdahls vei 8 B i Oslo, der eieren forteller om livet i huset. Fire minutter.":
        "An example of a Home Story: Heyerdahls vei 8 B in Oslo, where the owner talks about life in the house. Four minutes.",
    "La eieren fortelle.":
        "Let the owner tell it.",
    "Den som har bodd i huset, vet hvor morgensola kommer inn, hvor barna lekte og hvorfor de valgte akkurat det stedet. Det står ikke i salgsoppgaven, men det er ofte det kjøperen husker.":
        "The people who lived in the house know where the morning sun comes in, where the children played and why they chose that exact spot. It isn't in the sales brochure, but it's often what buyers remember.",
    "Kjøperen blir trygg":
        "Buyers feel confident",
    "Når eieren forteller, blir boligen et hjem og ikke bare et objekt. Det gjør det lettere å stole på den.":
        "When the owner tells the story, the property becomes a home rather than a listing. That makes it easier to trust.",
    "Noe å vise på befaringen":
        "Something to show the seller",
    "Megleren har et konkret tilbud til selgeren, med et ferdig eksempel å vise fram.":
        "The agent has a concrete offer for the seller, with a finished example to show.",
    "Fra opptak til ferdig film":
        "From shoot to finished film",
    "Vi filmer, fotograferer, flyr drone og redigerer selv. Du snakker med dem som gjør jobben.":
        "We film, photograph, fly the drone and edit ourselves. You talk to the people who do the work.",
    "Terrassen på Heyerdahls vei 8 B i kveldslys":
        "The terrace at Heyerdahls vei 8 B in evening light",
    "Huset og hagen sett fra luften, dronefoto":
        "The house and garden from the air, drone photo",
    "Bilder fra samme oppdrag, inne og ute, med drone og kveldsstemning.":
        "Photos from the same job, inside and out, with drone and evening light.",
    "Se hele prosjektet":
        "See the whole project",
    "Gå rundt selv.":
        "Walk around yourself.",
    "Med en 360-visning kan kjøperen gå fra rom til rom i sitt eget tempo, på mobilen eller på PC. Eksempelet under er fra en butikk, Amundsen Gulv i Oslo. I en bolig fungerer det på samme måte.":
        "With a 360 tour, buyers can move from room to room at their own pace, on a phone or a computer. The example below is from a shop, Amundsen Gulv in Oslo. In a home it works the same way.",
    "Salongen i butikken til Amundsen Gulv, fra 360-visningen":
        "The lounge in the Amundsen Gulv shop, from the 360 tour",
    "Åpne 360-visningen":
        "Open the 360 tour",
    "Åpne 360-visningen i et eget vindu":
        "Open the 360 tour in its own window",
    "360-visning fra en butikk: Amundsen Gulv":
        "360 tour of a shop: Amundsen Gulv",
    "To pakker.":
        "Two packages.",
    "Hva det koster, avhenger av boligen. Fortell oss litt om den, så sender vi et tilbud. Reise i Oslo, Bærum, Asker og Nordre Follo er med.":
        "The cost depends on the home. Tell us a little about it and we'll send you a quote. Travel within Oslo, Bærum, Asker and Nordre Follo is included.",
    "Anbefalt: med eieren i filmen":
        "Recommended: the owner in the film",
    "Boligfortelling":
        "Home Story",
    "Eieren forteller om livet i boligen. Forutsetter at eieren vil være med foran kamera.":
        "The owner talks about life in the home. Requires an owner who is happy to be on camera.",
    "Film der eieren forteller, 3 til 5 minutter":
        "A film in which the owner tells the story, 3 to 5 minutes",
    "Stående klipp av intervjuet, 40 til 60 sekunder, med teksting":
        "A vertical cut of the interview, 40 to 60 seconds, with subtitles",
    "Stående klipp på 15 til 20 sekunder uten tale, til sosiale medier":
        "A vertical clip of 15 to 20 seconds without speech, for social media",
    "Bilder inne og ute, med drone og kveldsstemning":
        "Photos inside and out, with drone and evening light",
    "360-visning, ligger ute i tre måneder":
        "A 360 tour, online for three months",
    "Be om tilbud":
        "Ask for a quote",
    "Når eieren ikke kan være med":
        "When the owner can't take part",
    "Meglerfilm":
        "Agent Film",
    "Reserven når eieren ikke vil eller kan stå foran kamera. Da er det megleren som viser boligen fram.":
        "The fallback when the owner won't or can't be on camera. Then the agent shows the home.",
    "Film der megleren viser boligen fram, 40 til 60 sekunder":
        "A film in which the agent shows the home, 40 to 60 seconds",
    "Bilder":
        "Photos",
    "Antallet følger boligen: 30 bilder for leilighet, 40 for hus og 50 for stor bolig. Trengs flere, legger vi dem til.":
        "The number follows the home: 30 photos for an apartment, 40 for a house and 50 for a large home. If more are needed, we add them.",
    "360-visningen":
        "The 360 tour",
    "Visningen ligger ute i tre måneder, og kan forlenges hvis boligen ikke er solgt.":
        "The tour stays online for three months and can be extended if the home hasn't sold.",
    "Levering":
        "Delivery",
    "Vi avtaler leveringen etter når boligen skal ut på markedet. Én runde med endringer i filmen er med.":
        "We agree on delivery based on when the home goes on the market. One round of changes to the film is included.",
    "Bruk":
        "Use",
    "Eieren og megleren kan bruke bildene og filmene i markedsføringen av boligen til den er solgt, i opptil tolv måneder.":
        "The owner and the agent can use the photos and films to market the home until it is sold, for up to twelve months.",
    "Arkitekturfoto.":
        "Architectural photography.",
    "Vanlige boligbilder viser hvert rom, så kjøperen får oversikten. Arkitekturfoto handler om selve bygget: formene, linjene og materialene, og hva arkitekten ville med dem.":
        "Standard property photos show every room, so buyers get the overview. Architectural photography is about the building itself: its shapes, lines and materials, and what the architect set out to do with them.",
    "Som tillegg":
        "As an add-on",
    "Når huset er tegnet med omhu, legger vi til arkitekturbilder ved siden av de vanlige. Annonsen får både oversikten og bildene som viser hva som gjør huset spesielt.":
        "When a house has been designed with real care, we add architectural photos alongside the standard set. The listing gets both the overview and the images that show what makes the house special.",
    "Mer tid og presisjon":
        "More time, more precision",
    "Hvert bilde settes opp på stativ, loddrette linjer står rett, og vi venter til lyset faller riktig på fasaden. Detaljer som en skyggelinje eller et møte mellom to materialer får egne bilder.":
        "Every shot is set up on a tripod, vertical lines stay straight, and we wait until the light falls right on the façade. Details like a shadow line or the point where two materials meet get photos of their own.",
    "Hjørnet av huset med balkong og glassrekkverk, arkitekturfoto":
        "The corner of the house with its balcony and glass railing, architectural photo",
    "Inngangspartiet med trekledning og murvegg, arkitekturfoto":
        "The entrance with timber cladding and a masonry wall, architectural photo",
    "Ring oss før befaringen, så har du noe å vise selgeren.":
        "Call us before you meet the seller, and you'll have something to show them.",
    "Skriv til oss":
        "Write to us",

    # about
    "Bak kamera siden 2023.": "Behind the camera since 2023.",
    "ZEJAKOV MEDIA ble startet av Jakov Zeljković. Siden 2023 har vi jobbet med foto og film for bedrifter, arrangementer og bryllup, og tatt produktbilder i studio.":
        "ZEJAKOV MEDIA was started by Jakov Zeljković. Since 2023 we've worked in photography and film for businesses, events and weddings, and shot product photography in the studio.",
    "Jakov har også filmet og vært med på å lage innhold for Izazovi Avanturu, en YouTube-kanal med over 40 millioner avspillinger og egen serie på Prime Video.":
        "Jakov has also filmed and helped create content for Izazovi Avanturu, a YouTube channel with more than 40 million views and its own series on Prime Video.",
    "I dag jobber vi nesten bare med boliger. Vi gjør hele jobben selv, fra opptak til klipp og farge. Vi holder til i Oslo, men tar oppdrag over hele verden.":
        "Today we work almost exclusively with homes. We handle the whole job ourselves, from shooting to editing and colour grading. We're based in Oslo, but we take on projects anywhere in the world.",
    "Ta kontakt": "Get in touch",

    # contact
    "Hva trenger du hjelp med?": "What do you need help with?",
    "E-post": "Email",
    "Telefon": "Phone",
    "Se omtaler på Google": "See reviews on Google",
    "Område": "Area",
    "Holder til i Oslo, tar oppdrag over hele verden": "Based in Oslo, working worldwide",
    "For eksempel hva som skal selges, og hva du vil at kjøperne skal legge merke til.": "For example, what's being sold and what you want buyers to notice.",
    "Adresse til boligen": "Property address",
    "Send forespørsel": "Send enquiry",
    "Du får svar innen 24 timer.": "You'll hear back within 24 hours.",
    "Fyll inn navn og e-post.": "Please fill in your name and email.",
    "Sjekk e-postadressen, den ser ikke riktig ut.": "Please check your email address, it doesn't look right.",
    "Sender …": "Sending …",
    "Takk. Meldingen er mottatt, og du hører fra oss innen 24 timer.": "Thank you. Your message has been received, and you'll hear from us within 24 hours.",
    "Noe gikk galt. Send heller en e-post til post@zejakov.com.": "Something went wrong. Please email us at post@zejakov.com instead.",

    # contact form questions
    "Noen korte spørsmål, så vet vi nok til å sende deg et tilbud. Du kan også ringe eller sende en e-post.": "A few short questions, and we'll know enough to send you a quote. You can also call or send an email.",
    "Spørsmål {n} av {t}": "Question {n} of {t}",
    "Spørsmål 1 av 7": "Question 1 of 7",
    "Hvem er du?": "Who are you?",
    "Megler": "Estate agent",
    "Eier som skal selge": "Owner selling the home",
    "Noe annet": "Something else",
    "Hva slags bolig er det?": "What kind of home is it?",
    "Leilighet": "Apartment",
    "Rekkehus eller tomannsbolig": "Terraced or semi-detached house",
    "Enebolig": "Detached house",
    "Fritidsbolig": "Holiday home",
    "Omtrent hvor stor er den?": "Roughly how big is it?",
    "Under 60 m²": "Under 60 m²",
    "60 til 120 m²": "60 to 120 m²",
    "120 til 250 m²": "120 to 250 m²",
    "Over 250 m²": "Over 250 m²",
    "Hva ser du for deg?": "What do you have in mind?",
    "Eieren forteller i filmen": "The owner tells the story in the film",
    "Megleren viser boligen": "The agent shows the home",
    "Bare bilder": "Photos only",
    "Med drone og kveldsstemning": "With drone and evening light",
    "Vet ikke ennå": "Not sure yet",
    "Vi gir deg et råd": "We'll give you our advice",
    "Når skal boligen ut på markedet?": "When does the home go on the market?",
    "Innen to uker": "Within two weeks",
    "Innen en måned": "Within a month",
    "Senere": "Later",
    "Noe mer vi bør vite?": "Anything else we should know?",
    "Hvor sender vi tilbudet?": "Where should we send the quote?",
    "Tilbake": "Back",

    "Enebolig i Oslo med utsikt over byen. Eieren forteller om livet i huset, med bilder og drone fra samme oppdrag.":
        "A detached house in Oslo overlooking the city. The owner talks about life in the house, with photos and drone footage from the same project.",
    # privacy
    "Hva vi lagrer, og hvorfor.": "What we store, and why.",
    "Bare det du selv sender oss, og bare så lenge jobben krever det.": "Only what you send us yourself, and only for as long as the job requires.",
    "Hvem som står bak": "Who is responsible",
    "ZEJAKOV ZELJKOVIC, organisasjonsnummer 835 196 542, Oslo. Spørsmål om personvern går til post@zejakov.com.":
        "ZEJAKOV ZELJKOVIC, organisation number 835 196 542, Oslo. Questions about privacy go to post@zejakov.com.",
    "Informasjonskapsler": "Cookies",
    "Siden setter ingen. Den lagrer heller ingenting annet i nettleseren din, og det finnes ingen annonsesporing. Vi teller bare anonymt hvor mange som besøker sidene og trykker på telefon, e-post, Instagram og booking, og om besøket kom fra for eksempel et søk eller Instagram. Det skjer uten informasjonskapsler og uten at vi vet hvem du er. Skriftene ligger på vår egen server, så ingen tredjepart får vite at du var innom. Derfor slipper du samtykkeboksen.":
        "The site doesn't set any. It doesn't store anything else in your browser either, and there is no ad tracking. We only count, anonymously, how many people visit the pages and tap the phone number, email, Instagram and booking links, and whether the visit came from, say, a search or Instagram. This happens without cookies and without us knowing who you are. The fonts are hosted on our own server, so no third party learns that you stopped by. That's why there is no consent banner.",
    "Kontaktskjemaet": "The contact form",
    "Sender du skjemaet, lagrer vi navn, e-post, telefon, adressen på boligen, svarene dine og meldingen din, sammen med hvor besøket kom fra, for eksempel Instagram eller et søk. Det brukes til å svare deg og gjennomføre oppdraget. Grunnlaget er forespørselen din og en berettiget interesse i å drive virksomheten. Opplysningene slettes når saken er avsluttet, og senest etter tolv måneder uten kontakt. Blir det et oppdrag, må bilagene oppbevares så lenge bokføringsloven krever.":
        "If you send the form, we store your name, email, phone number, the property address, your answers and your message, along with where the visit came from, such as Instagram or a search. This is used to reply to you and to carry out the job. The legal basis is your enquiry and a legitimate interest in running the business. The information is deleted once the matter is closed, and at the latest after twelve months without contact. If it becomes a job, the accounting records must be kept for as long as the Norwegian Bookkeeping Act requires.",
    "Vurderinger": "Reviews",
    "Legger du igjen en vurdering, lagres navnet du oppgir, stjernene og teksten. Den vises først når vi har godkjent den. Vil du ha den fjernet, si fra, så er den borte.":
        "If you leave a review, the name you give, the stars and the text are stored. It only appears once we've approved it. If you want it removed, just tell us and it's gone.",
    "Hvem som ellers ser opplysningene": "Who else sees the information",
    "Nettstedet driftes av Hostinger. Skjemaer og vurderinger lagres hos Supabase på servere i Stockholm, altså innenfor EØS. Varsel om nye henvendelser sendes på e-post gjennom Resend, som kan behandle dem utenfor EØS etter EUs standard personvernbestemmelser. Alle tre arbeider på våre vegne. Ingenting selges eller deles videre.":
        "The website is hosted by Hostinger. Forms and reviews are stored with Supabase on servers in Stockholm, within the EEA. Notifications of new enquiries are sent by email through Resend, which may process them outside the EEA under the EU's standard contractual clauses. All three work on our behalf. Nothing is sold or passed on.",
    "Filmer fra YouTube": "Films from YouTube",
    "Filmene ligger på YouTube. Før du trykker på spill av, ser du bare et bilde fra vår egen server, og ingenting sendes til YouTube. Trykker du, lastes filmen fra youtube-nocookie.com, og da gjelder Googles personvernregler for avspillingen.":
        "The films are hosted on YouTube. Before you press play, you only see an image from our own server, and nothing is sent to YouTube. Once you press play, the film loads from youtube-nocookie.com, and Google's privacy policy applies to the playback.",
    "Bilder og film": "Photos and film",
    "Opptak fra et oppdrag brukes i markedsføringen av boligen det gjelder. Skal vi også vise dem i vårt eget arbeid, avtaler vi det først. Er det mennesker i bildet, spør vi før vi bruker det. Bilder og film på denne siden er våre egne, og kan ikke brukes uten avtale.":
        "Footage from a job is used to market the home in question. If we also want to show it in our own portfolio, we agree on that first. If there are people in a shot, we ask before we use it. The photos and films on this site are our own and may not be used without permission.",
    "Rettighetene dine": "Your rights",
    "Du kan be om innsyn i det som er lagret om deg, få det rettet eller slettet, be om en kopi, og protestere mot at vi bruker det. Send en e-post, så ordner vi det. Mener du at vi gjør noe galt, kan du klage til Datatilsynet.":
        "You can ask to see what is stored about you, have it corrected or deleted, ask for a copy, and object to our using it. Send us an email and we'll sort it out. If you think we're doing something wrong, you can complain to Datatilsynet, the Norwegian Data Protection Authority.",
    "Sist oppdatert 4. november 2026.": "Last updated 4 November 2026.",
}

# plain replacements for the few pieces that are not a whole text, attribute or string
RAW = [
    ('<html lang="nb">', '<html lang="en">'),
    ('<meta property="og:locale" content="nb_NO">', '<meta property="og:locale" content="en_GB">'),
    ('alt="${f.t}, Heyerdahls vei 8 B i Oslo"', 'alt="${f.t}, Heyerdahls vei 8 B in Oslo"'),
    ('.replace(/^Spill av filmen: /, "")', '.replace(/^Play the film: /, "")'),
    ('"url": "https://zejakov.com/arbeid/heyerdahls-vei-8b/"', '"url": "https://zejakov.com/en/work/heyerdahls-vei-8b/"'),
]
