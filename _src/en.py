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
             "for viewings and listings, all done by one person. See the work and book a call."),
    "arbeid": ("Work: property film and photography from Oslo | ZEJAKOV MEDIA",
               "Homes I have photographed and filmed in and around Oslo. Each project "
               "includes film, photos and drone footage."),
    "heyerdahls": ("Heyerdahls vei 8 B: property film from Oslo | ZEJAKOV MEDIA",
                   "A detached house in Oslo overlooking the city. Film, photos and drone "
                   "footage from the same project, August 2026."),
    "tjenester": ("Property film, photography and drone in Oslo | ZEJAKOV MEDIA",
                  "The whole job done by one person: photos, film, drone and lighting. For "
                  "owners and agents who want to show what it is like to live in the home."),
    "om": ("Property photographer and filmmaker in Oslo | ZEJAKOV MEDIA",
           "Photography and film since 2023, now almost entirely homes. Based in Oslo, "
           "working worldwide."),
    "kontakt": ("Book a call about property film in Oslo | ZEJAKOV MEDIA",
                "Tell me about the home and we will set up a call. Property "
                "film, photography and drone in Oslo, and projects worldwide."),
    "personvern": ("Privacy | ZEJAKOV MEDIA",
                   "What I store and why. The site sets no cookies and has no tracking."),
}

# whole pieces of text, Norwegian -> English
T = {
    # head
    "Enebolig i Oslo filmet av ZEJAKOV MEDIA": "A detached house in Oslo filmed by ZEJAKOV MEDIA",
    "Medieproduksjon for eiendom i Oslo. Boligfilm, boligfoto og drone til visning og annonse, alt gjort av samme person. Se arbeidet og book befaring.":
        "Media production for property in Oslo. Film, photography and drone footage for viewings and listings, all done by one person. See the work and book a call.",
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
    "Om meg": "About",
    "Kontakt": "Contact",
    "Book befaring": "Book a call",
    "Meny": "Menu",
    "Lukk": "Close",
    "Bytt til lyst tema": "Switch to light mode",
    "Bytt til mørkt tema": "Switch to dark mode",
    "Språk": "Language",
    "ZEJAKOV ZELJKOVIC, org. 835 196 542": "ZEJAKOV ZELJKOVIC, org. no. 835 196 542",
    "Personvern": "Privacy",
    "Ring 973 44 658": "Call 973 44 658",

    # home: hero
    "Hver bolig har en historie.": "Every home has a story.",
    "La oss fortelle den.": "Let's tell it.",
    "Holder det med en vanlig annonse, er dette feil firma for deg.": "If a standard listing is all you need, I'm not the right fit.",
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
    "Et hus til 35 millioner": "A NOK 35 million home",
    "skal ikke se ut som et til 5.": "shouldn't look like a 5 million one.",
    "Det er ikke mange kjøpere i den prisklassen, og de har allerede sett hundrevis av annonser med sjelløse rom og flatt lys. Jeg lager bilder og film som forteller historien om boligen og viser hvordan det er å leve der. Det er det som får den til å skille seg ut.":
        "There aren't many buyers at that price, and they have already scrolled past hundreds of listings full of lifeless rooms and flat light. I make photos and film that tell the story of the home and show what it's like to live there. That is what makes it stand out.",

    # home: one house at a time
    "Ett hus om gangen.": "One house at a time.",
    "Mange meglerkjeder har faste fotoavtaler der det handler om å rekke flest mulig boliger hver dag. Fotografen har ofte rundt en time i hver bolig før det er videre til neste adresse. Det gir mange annonser, men sjelden en bolig som skiller seg ut.":
        "Many estate agency chains have fixed photography deals built around getting through as many homes as possible each day. The photographer often has about an hour in each home before moving on to the next address. You end up with plenty of listings, but rarely a home that stands out.",
    "Jeg jobber motsatt. Jeg tar bare et begrenset antall boliger i måneden, så hvert hus får den tiden og oppmerksomheten det fortjener. Jeg venter på riktig lys, finner vinklene som viser hvordan det er å bo der, og redigerer hver bolig for seg.":
        "I work the other way round. I only take on a limited number of homes each month, so every house gets the time and attention it deserves. I wait for the right light, find the angles that show what it's like to live there, and edit every home individually.",
    "Få boliger i måneden": "A few homes a month",
    "Jeg tar et begrenset antall oppdrag, så hvert hus får full oppmerksomhet.": "I take on a limited number of jobs, so every house gets my full attention.",
    "Ingen stoppeklokke": "No rush",
    "Jeg blir til bildene sitter, uten en ny adresse som venter.": "I stay until the shots are right. There's no next address waiting.",
    "Samme person hele veien": "One person, start to finish",
    "Den du snakker med, er den som fotograferer, filmer og redigerer.": "The person you talk to is the one who shoots, films and edits.",

    # home: before / after
    "To versjoner av samme rom.": "Two versions of the same room.",
    "Til venstre: standard HDR, slik de fleste boligbilder ser ut. Flatt og jevnt lyst, der alt er like viktig. Det er ikke noe galt med det, men det blir fort borte blant alle de andre annonsene. Det jeg lager, skiller seg ut.":
        "On the left: standard HDR, the way most property photos look. Flat and evenly lit, with everything given the same weight. There's nothing wrong with it, but it gets lost among all the other listings. What I make stands out.",
    "Soverom, Heyerdahls vei 8 B": "Bedroom, Heyerdahls vei 8 B",
    "Soverom i enebolig i Oslo, redigert av ZEJAKOV MEDIA": "Bedroom in a detached house in Oslo, edited by ZEJAKOV MEDIA",
    "Samme soverom med standard HDR": "The same bedroom with standard HDR",
    "Kjøkken og spisestue, samme bolig": "Kitchen and dining room, same home",
    "Kjøkken og spisestue i enebolig i Oslo, redigert av ZEJAKOV MEDIA": "Kitchen and dining room in a detached house in Oslo, edited by ZEJAKOV MEDIA",
    "Samme kjøkken og spisestue med standard HDR": "The same kitchen and dining room with standard HDR",
    "Dra i bildet": "Drag the image",
    "Til høyre er slik jeg leverer. Hvert hus redigeres for seg, slik at farger, lys og stemning blir som når du står i rommet. Det gir et mer personlig og redaksjonelt uttrykk, og et riktigere bilde av boligen.":
        "On the right is what I deliver. Every house is edited on its own, so the colour, light and mood match what you see when you stand in the room. The result feels more personal and editorial, and gives a truer picture of the home.",
    "I boligfoto er det vanlig å fjerne alle fargestikk, så veggene blir helt hvite. For leiligheter og mindre boliger er det ofte riktig valg, og det leverer jeg gjerne.":
        "In property photography it's common to remove every colour cast so the walls come out pure white. For flats and smaller homes that is often the right call, and I'm happy to deliver it.",
    "I dyrere boliger er lys og materialer valgt med omhu. Det varme lyset fra lampene og det grønne fra hagen er en del av huset, og da er det en feil å vaske det bort. Gjort riktig er det nettopp det som gir bildet liv.":
        "In higher-end homes, the lighting and materials have been chosen with care. The warm glow of the lamps and the green from the garden are part of the house, so washing them out is a mistake. Done right, that is exactly what brings a photo to life.",

    # virtual staging (home and project)
    "Samme rom, flere muligheter.": "One room, many possibilities.",
    "Digital møblering. Tomme rom kan jeg møblere digitalt. Fulle rom kan jeg tømme på bildet og møblere på nytt, så kjøperen ser hva rommet kan brukes til. Selve rommet, med vegger, dører og vinduer, blir som det er. Eksempelet er aktivitetsrommet i kjelleren på Heyerdahls vei 8 B, tømt og møblert på fire måter.":
        "Virtual staging. I can furnish empty rooms digitally, and empty furnished rooms in the photo and restyle them, so buyers can see what a room could be used for. The room itself, with its walls, doors and windows, stays exactly as it is. The example is the basement activity room at Heyerdahls vei 8 B, emptied and furnished four different ways.",
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
    "Fortell meg om boligen, så tar vi det derfra.": "Tell me about the home, and we'll take it from there.",

    # work
    "Boliger jeg har filmet.": "Homes I've filmed.",
    "Film og bilder fra oppdrag i Oslo og omegn.": "Film and photos from projects in and around Oslo.",
    "Heyerdahls vei 8 B: fasaden mot hagen": "Heyerdahls vei 8 B: the façade facing the garden",
    "Enebolig i Oslo med utsikt over byen. Film, bilder og drone fra samme oppdrag.": "A detached house in Oslo overlooking the city. Film, photos and drone footage, all from the same project.",

    # project page
    "Spill av filmen: Heyerdahls vei 8 B": "Play the film: Heyerdahls vei 8 B",
    "Huset ligger høyt og har utsikt over Oslo. Film, bilder, drone og klipp er gjort av meg.": "The house sits high above the city, with all of Oslo laid out below. I shot the film, the photos and the drone footage, and did the editing myself.",
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
    "Jeg selger ikke pene filmer.": "I don't sell pretty films.",
    "Jeg hjelper deg å selge boligen.": "I help you sell the home.",
    "Skal du bare ha bilder og film som alle andre, finnes det mange som gjør den jobben, og de gjør den billigere enn meg.":
        "If you just want the same photos and film as everyone else, plenty of people can do that job, and they'll do it for less than I will.",
    "Er du eier eller megler og vil at riktig kjøper skal kjenne på hvordan det er å bo der, gjør vi noe annet.":
        "If you're an owner or an agent and want the right buyer to feel what it's like to live there, we'll do something different.",
    "Heyerdahls vei 8 B i Oslo sett fra luften, dronefoto": "Heyerdahls vei 8 B in Oslo seen from the air, drone photo",
    "Boligen er hovedpersonen.": "The home is the main character.",
    "Jeg gjør hele jobben selv: bilder, film og drone, med flere kameraer og eget lys når rommet trenger det.":
        "I do the whole job myself: photos, film and drone, with several cameras and my own lighting when a room needs it.",
    "Formen avhenger av boligen. Noen ganger passer stående klipp best, andre ganger en lengre film med kinopreg, og noen ganger en video der megleren viser boligen fram. Det finner vi ut sammen på befaringen.":
        "The format depends on the home. Sometimes vertical clips work best, sometimes a longer, cinematic film, and sometimes a video where the agent shows viewers around. We'll work that out together when we talk.",
    "Går en film viralt, er det fint, men det er ikke poenget. Uansett form er det boligen som står i sentrum, ikke antall avspillinger.":
        "If a film goes viral, great, but that's not the point. Whatever the format, the home is the focus, not the view count.",
    "Redaksjonelle bilder.": "Editorial photos.",
    "Vanlige boligbilder viser hvert rom fra hjørnet, så kjøperen får oversikten. Redaksjonelle bilder er tatt som i et interiørmagasin. De går tettere på materialer og lys, og viser hvordan det er å bo der.":
        "Standard property photos show each room from the corner, so buyers get the overview. Editorial photos are shot like the pictures in an interiors magazine. They get closer to the materials and the light, and show what it's like to live there.",
    "Som tillegg": "As an add-on",
    "Fem eller ti redaksjonelle bilder i tillegg til de vanlige. Annonsen får både oversikten kjøperne leter etter, og bildene som får dem til å stoppe opp.":
        "Five or ten editorial photos on top of the standard set. The listing gets both the overview buyers are looking for and the images that make them stop scrolling.",
    "I stedet for vanlige bilder": "Instead of standard photos",
    "Hele settet tas i redaksjonell stil. Det passer når arkitekturen og interiøret er en stor del av det kjøperen betaler for.":
        "The whole set is shot in an editorial style. This suits homes where the architecture and interiors are a big part of what the buyer is paying for.",
    "Hva som passer for din bolig, finner vi ut sammen.": "We'll work out together what suits your home.",
    "Bad med badekar og høyt vindu, redaksjonelt bilde": "Bathroom with a bathtub and a tall window, editorial photo",
    "Nattbord og lampe på soverommet, redaksjonelt bilde": "Bedside table and lamp in the bedroom, editorial photo",
    "Bilder og film er bare verktøyet. Det som teller, er salget.": "Photos and film are just the tools. What counts is the sale.",

    # about
    "Bak kamera siden 2023.": "Behind the camera since 2023.",
    "Jeg heter Jakov, og det er jeg som står bak ZEJAKOV MEDIA. Siden 2023 har jeg jobbet med foto og film for bedrifter, arrangementer og bryllup, og tatt produktbilder i studio.":
        "I'm Jakov, the person behind ZEJAKOV MEDIA. Since 2023 I've worked in photography and film for businesses, events and weddings, and shot product photography in the studio.",
    "Jeg har også filmet og vært med på å lage innhold for Izazovi Avanturu, en YouTube-kanal med over 40 millioner avspillinger og egen serie på Prime Video.":
        "I've also filmed and helped create content for Izazovi Avanturu, a YouTube channel with more than 40 million views and its own series on Prime Video.",
    "I dag jobber jeg nesten bare med boliger. Jeg gjør hele jobben selv, fra opptak til klipp og farge, så du forholder deg bare til meg. Jeg holder til i Oslo, men tar oppdrag over hele verden.":
        "Today I work almost exclusively with homes. I handle the whole job myself, from shooting to editing and colour grading, so you only ever deal with me. I'm based in Oslo, but I take on projects anywhere in the world.",
    "Ta kontakt": "Get in touch",

    # contact
    "Hva trenger du hjelp med?": "What do you need help with?",
    "Skriv kort hva du trenger og hva du vil oppnå. Jeg legger opp hver jobb etter det, så ser jeg om jeg kan hjelpe deg.":
        "Tell me briefly what you need and what you want to achieve. I plan every job around that, and I'll let you know if I can help.",
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
    "Takk. Meldingen er mottatt, og du hører fra meg innen 24 timer.": "Thank you. Your message has been received, and you'll hear from me within 24 hours.",
    "Noe gikk galt. Send heller en e-post til post@zejakov.com.": "Something went wrong. Please email me at post@zejakov.com instead.",

    # privacy
    "Hva jeg lagrer, og hvorfor.": "What I store, and why.",
    "Bare det du selv sender meg, og bare så lenge jobben krever det.": "Only what you send me yourself, and only for as long as the job requires.",
    "Hvem som står bak": "Who is responsible",
    "ZEJAKOV ZELJKOVIC, organisasjonsnummer 835 196 542, Oslo. Spørsmål om personvern går til post@zejakov.com.":
        "ZEJAKOV ZELJKOVIC, organisation number 835 196 542, Oslo. Questions about privacy go to post@zejakov.com.",
    "Informasjonskapsler": "Cookies",
    "Siden setter ingen. Den lagrer heller ingenting annet i nettleseren din, og det finnes ingen annonsesporing. Jeg teller bare anonymt hvor mange som besøker sidene og trykker på telefon, e-post, Instagram og booking, og om besøket kom fra for eksempel et søk eller Instagram. Det skjer uten informasjonskapsler og uten at jeg vet hvem du er. Skriftene ligger på min egen server, så ingen tredjepart får vite at du var innom. Derfor slipper du samtykkeboksen.":
        "The site doesn't set any. It doesn't store anything else in your browser either, and there is no ad tracking. I only count, anonymously, how many people visit the pages and tap the phone number, email, Instagram and booking links, and whether the visit came from, say, a search or Instagram. This happens without cookies and without me knowing who you are. The fonts are hosted on my own server, so no third party learns that you stopped by. That's why there is no consent banner.",
    "Kontaktskjemaet": "The contact form",
    "Sender du skjemaet, lagrer jeg navn, e-post, telefon, adressen på boligen og meldingen din, sammen med hvor besøket kom fra, for eksempel Instagram eller et søk. Det brukes til å svare deg og gjennomføre oppdraget. Grunnlaget er forespørselen din og en berettiget interesse i å drive virksomheten. Opplysningene slettes når saken er avsluttet, og senest etter tolv måneder uten kontakt. Blir det et oppdrag, må bilagene oppbevares så lenge bokføringsloven krever.":
        "If you send the form, I store your name, email, phone number, the property address and your message, along with where the visit came from, such as Instagram or a search. This is used to reply to you and to carry out the job. The legal basis is your enquiry and a legitimate interest in running the business. The information is deleted once the matter is closed, and at the latest after twelve months without contact. If it becomes a job, the accounting records must be kept for as long as the Norwegian Bookkeeping Act requires.",
    "Vurderinger": "Reviews",
    "Legger du igjen en vurdering, lagres navnet du oppgir, stjernene og teksten. Den vises først når jeg har godkjent den. Vil du ha den fjernet, si fra, så er den borte.":
        "If you leave a review, the name you give, the stars and the text are stored. It only appears once I've approved it. If you want it removed, just tell me and it's gone.",
    "Hvem som ellers ser opplysningene": "Who else sees the information",
    "Nettstedet driftes av Hostinger. Skjemaer og vurderinger lagres hos Supabase på servere i Stockholm, altså innenfor EØS. Varsel om nye henvendelser sendes på e-post gjennom Resend, som kan behandle dem utenfor EØS etter EUs standard personvernbestemmelser. Alle tre arbeider på mine vegne. Ingenting selges eller deles videre.":
        "The website is hosted by Hostinger. Forms and reviews are stored with Supabase on servers in Stockholm, within the EEA. Notifications of new enquiries are sent by email through Resend, which may process them outside the EEA under the EU's standard contractual clauses. All three work on my behalf. Nothing is sold or passed on.",
    "Filmer fra YouTube": "Films from YouTube",
    "Filmene ligger på YouTube. Før du trykker på spill av, ser du bare et bilde fra min egen server, og ingenting sendes til YouTube. Trykker du, lastes filmen fra youtube-nocookie.com, og da gjelder Googles personvernregler for avspillingen.":
        "The films are hosted on YouTube. Before you press play, you only see an image from my own server, and nothing is sent to YouTube. Once you press play, the film loads from youtube-nocookie.com, and Google's privacy policy applies to the playback.",
    "Bilder og film": "Photos and film",
    "Opptak fra et oppdrag brukes i markedsføringen av boligen det gjelder. Skal jeg også vise dem i mitt eget arbeid, avtaler vi det først. Er det mennesker i bildet, spør jeg før jeg bruker det. Bilder og film på denne siden er mine egne, og kan ikke brukes uten avtale.":
        "Footage from a job is used to market the home in question. If I also want to show it in my own portfolio, we agree on that first. If there are people in a shot, I ask before I use it. The photos and films on this site are my own and may not be used without permission.",
    "Rettighetene dine": "Your rights",
    "Du kan be om innsyn i det som er lagret om deg, få det rettet eller slettet, be om en kopi, og protestere mot at jeg bruker det. Send en e-post, så ordner jeg det. Mener du at jeg gjør noe galt, kan du klage til Datatilsynet.":
        "You can ask to see what is stored about you, have it corrected or deleted, ask for a copy, and object to my using it. Send me an email and I'll sort it out. If you think I'm doing something wrong, you can complain to Datatilsynet, the Norwegian Data Protection Authority.",
    "Sist oppdatert 26. september 2026.": "Last updated 26 September 2026.",
}

# plain replacements for the few pieces that are not a whole text, attribute or string
RAW = [
    ('<html lang="nb">', '<html lang="en">'),
    ('<meta property="og:locale" content="nb_NO">', '<meta property="og:locale" content="en_GB">'),
    ('alt="${f.t}, Heyerdahls vei 8 B i Oslo"', 'alt="${f.t}, Heyerdahls vei 8 B in Oslo"'),
    ('.replace(/^Spill av filmen: /, "")', '.replace(/^Play the film: /, "")'),
    ('"url": "https://zejakov.com/arbeid/heyerdahls-vei-8b/"', '"url": "https://zejakov.com/en/work/heyerdahls-vei-8b/"'),
]
