from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape


PAGES = [
    ["?????","ABeeZee","ADLaM Display","AR One Sans","Abel","Abhaya Libre","Abhaya Libre ExtraBold","Abhaya Libre Medium","Abhaya Libre SemiBold","Aboreto","Abril Fatface","Abyssinica SIL","Aclonica","Acme","Actor","Adamina","Adobe Blank","Advent Pro","Afacad","Agbalumo","Agdasima","Aguafina Script","Akatab","Akaya Kanadaka","Akaya Telivigala","Akronim","Aksara Bali Galang","Akshar","Aladin","Alata","Alatsi","Albert Sans","Aldrich","Alef","Alegreya","Alegreya SC","Alegreya Sans","Alegreya Sans SC","Aleo","Alex Brush","Alexandria","Alfa Slab One","Alice","Alike","Alike Angular","Alkalami","Alkatra","Allan","Allerta","Allerta Stencil","Allison","Allura","Almarai","Almendra","Almendra Display","Almendra SC","Alumni Sans","Alumni Sans Collegiate One","Alumni Sans Collegiate One SC","Alumni Sans Inline One","Alumni Sans Pinstripe","Alumni Sans SC","Amarante","Amaranth","Amatic SC","Amatica SC","Amethysta","Amiko","Amiri","Amiri Quran","Amiri Quran Colored","Amita","AmstelvarAlpha","Anaheim","Andada Pro","Andika","Andika New Basic","Anek Bangla","Anek Devanagari","Anek Gujarati","Anek Gurmukhi","Anek Kannada","Anek Latin","Anek Malayalam","Anek Odia","Anek Tamil","Anek Telugu","Angkor","Annapurna SIL","Annie Use Your Telescope","Anonymous Pro","Anta","Antic","Antic Didone","Antic Slab","Anton","Anton SC","Antonio","Anuphan","Anybody","Aoboshi One","Arapey","Arbutus","Arbutus Slab","Architects Daughter","Archivo","Archivo Black","Archivo Narrow","Are You Serious","Aref Ruqaa","Aref Ruqaa Ink","Arima","Arima Madurai","Arimo","Arimo Hebrew Subset","Arimo Hebrew Subset Italic","Arizonia","Armata","Arsenal","Arsenal SC","Artifika","Arvo","Arya","Asap","Asap Condensed","Asar","Asset","Assistant","Astloch","Asul","Athiti","Atkinson Hyperlegible","Atma","Atomic Age","Aubrey","Audiowide","Autour One","Average","Average Sans","Averia Gruesa Libre","Averia Libre","Averia Sans Libre","Averia Serif Libre","Azeret Mono","B612","B612 Mono","BIZ UDGothic","BIZ UDMincho","BIZ UDPGothic","BIZ UDPMincho","BM HANNA_TTF","Babylonica","Bacasime Antique","Bad Script","Bagel Fat One","Bahiana","Bahianita","Bai Jamjuree","Bakbak One","Ballet","Baloo","Baloo 2","Baloo Bhai","Baloo Bhai 2","Baloo Bhaijaan","Baloo Bhaijaan 2","Baloo Bhaina","Baloo Bhaina 2","Baloo Chettan","Baloo Chettan 2","Baloo Da","Baloo Da 2","Baloo Paaji","Baloo Paaji 2","Baloo Tamma","Baloo Tamma 2","Baloo Tammudu","Baloo Tammudu 2","Baloo Thambi","Baloo Thambi 2","Balsamiq Sans","Balthazar","Bangers","Barlow","Barlow Condensed","Barlow Semi Condensed","Barriecito","Barrio","Basic","Baskervville","Baskervville SC","Battambang","Baumans","Bayon","Be Vietnam","Be Vietnam Pro","Beau Rivage","Bebas Neue","Beiruti","Belanosima","Belgrano","Bellefair","Belleza","Bellota","Bellota Text","BenchNine","Benne","Bentham","Berkshire Swash","Besley","Beth Ellen","Bevan","Bhavuka","BhuTuka Expanded One","Big Shoulders Display","Big Shoulders Inline Display","Big Shoulders Inline Text","Big Shoulders Stencil Display","Big Shoulders Stencil Text","Big Shoulders Text","Bigelow Rules","Bigshot One","Bilbo","Bilbo Swash Caps","BioRhyme","BioRhyme Expanded","Birthstone","Birthstone Bounce","Biryani","Bitter","Black And White Picture","Black Han Sans","Black Ops One","Blaka","Blaka Hollow","Blaka Ink","Blinker","Bodoni Moda","Bodoni Moda SC","Bokor","Bona Nova","Bona Nova SC","Bonbon","Bonheur Royale","Boogaloo","Borel","Bowlby One","Bowlby One SC","Braah One","Brawler","Bree Serif","Bricolage Grotesque","Briem Hand","Bruno Ace","Bruno Ace SC","Brygada 1918","Bubblegum Sans","Bubbler One","Buda","Buenard","Bungee","Bungee Color","Bungee Hairline","Bungee Inline","Bungee Outline","Bungee Shade","Bungee Spice","Butcherman","Butcherman Caps","Butterfly Kids","Cabin","Cabin Condensed","Cabin Sketch","Cactus Classical Serif","Caesar Dressing","Cagliostro","Cairo","Cairo Play","Caladea","Calistoga","Calligraffitti","Cambay","Cambo","Candal","Cantarell","Cantata One","Cantora One","CantoraOne","Caprasimo","Capriola","Caramel","Carattere","Cardo","Carlito","Carme","Carrois Gothic","Carrois Gothic SC","Carter One","Castoro","Castoro Titling"],
    ["Catamaran","Caudex","Caveat","Caveat Brush","Cedarville Cursive","Ceviche One","Chakra Petch","Changa","Changa One","Chango","Charis SIL","Charm","Charmonman","Chathura","Chau Philomene One","Chela One","Chelsea Market","Chenla","Cherish","Cherry Bomb","Cherry Bomb One","Cherry Cream Soda","Cherry Swash","Chewy","Chicle","Chilanka","Chivo","Chivo Mono","Chocolate Classical Sans","Chokokutai","Chonburi","Cinzel","Cinzel Decorative","Clicker Script","Climate Crisis","Coda","Coda Caption","Codystar","Coiny","Combo","Comfortaa","Comforter","Comforter Brush","Comic Neue","Coming Soon","Comme","Commissioner","Concert One","Condiment","Content","Contrail One","Convergence","Cookie","Copse","Corben","Corinthia","Cormorant","Cormorant Garamond","Cormorant Infant","Cormorant SC","Cormorant Unicase","Cormorant Upright","Courgette","Courier Prime","Cousine","Coustard","Covered By Your Grace","Crafty Girls","Creepster","Creepster Caps","Crete Round","Crimson Pro","Crimson Text","Croissant One","Crushed","Cuprum","Cute Font","Cutive","Cutive Mono","DM Mono","DM Sans","DM Serif Display","DM Serif Text","Dai Banna SIL","Damion","Dancing Script","Danfo","Dangrek","Darker Grotesque","Darumadrop One","David Libre","Dawning of a New Day","Days One","Decovar Alpha","Dekko","Dela Gothic One","Delicious Handrawn","Delius","Delius Swash Caps","Delius Unicase","Della Respira","Denk One","Devonshire","Dhurjati","Dhyana","Didact Gothic","Digital Numbers","Diphylleia","Diplomata","Diplomata SC","Do Hyeon","Dokdo","Domine","Donegal One","Dongle","Doppio One","Dorsa","Dosis","DotGothic16","Dr Sugiyama","Droid Sans","Duru Sans","DynaPuff","Dynalight","EB Garamond","Eagle Lake","East Sea Dokdo","Eater","Economica","Eczar","Edu AU VIC WA NT Hand","Edu NSW ACT Foundation","Edu QLD Beginner","Edu SA Beginner","Edu TAS Beginner","Edu VIC WA NT Beginner","Ek Mukta","El Messiri","Electrolize","Elsie","Elsie Swash Caps","Emblema One","Emilys Candy","Encode Sans","Encode Sans Condensed","Encode Sans Expanded","Encode Sans SC","Encode Sans Semi Condensed","Encode Sans Semi Expanded","Engagement","Englebert","Enriqueta","Ephesis","Epilogue","Erica One","Esteban","Estedad-VF","Estonia","Euphoria Script","Ewert","Exo","Exo 2","Expletus Sans","Explora","Fahkwang","Familjen Grotesk","Fanwood Text","Farro","Farsan","Fascinate","Fascinate Inline","Faster One","Fasthand","Fauna One","Faustina","Federant","Federo","Felipa","Fenix","Festive","Figma Hand","Figtree","Finger Paint","Finlandica","Fira Code","Fira Mono","Fira Sans","Fira Sans Condensed","Fira Sans Extra Condensed","Fjalla One","Fjord","Flamenco","Flavors","Fleur De Leah","Flow Block","Flow Circular","Flow Rounded","Foldit","Fondamento","Font Awesome 5 Brands","Font Awesome 5 Free","Font Awesome 6 Brands","Font Awesome 6 Free","Fontdiner Swanky","Forum","Fragment Mono","Francois One","Frank Ruhl Libre","Fraunces","Freckle Face","Fredericka the Great","Fredoka","Fredoka One","Freehand","Freeman","Fresca","Frijole","Fruktur","Fugaz One","Fuggles","Fustat","Fuzzy Bubbles","GFS Didot","GFS Neohellenic","Ga Maamli","Gabarito","Gabriela","Gaegu","Gafata","Gajraj One","Galada","Galdeano","Galindo","Gamja Flower","Gantari","Gasoek One","Gayathri","Geist","Geist Mono","Gelasio","Gemunu Libre","Genos","Gentium Basic","Gentium Book Basic","Gentium Book Plus","Gentium Plus","Geo","Geologica","Georama","Geostar","Geostar Fill","Germania One","Gideon Roman","Gidugu","Gilda Display","Girassol","Give You Glory","Glass Antiqua","Glegoo","Gloock","Gloria Hallelujah","Glory","Gluten","Goblin One","Gochi Hand","Goldman","Golos Text","Gorditas","Gothic A1","Gotu","Goudy Bookletter 1911","Gowun Batang","Gowun Dodum","Graduate","Grand Hotel","Grandiflora One","Grandstander","Grape Nuts","Gravitas One","Great Vibes","Grechen Fuemen","Grenze","Grenze Gotisch","Grey Qo","Griffy","Gruppo","Gudea","Gugi","Gulzar","Gupter","Gurajada","Gwendolyn","Habibi","Hachi Maru Pop","Hahmlet","Halant","Hammersmith One","Hanalei","Hanalei Fill","Handjet"],
    ["Handlee","Hanken Grotesk","Hannari","Hanuman","Happy Monkey","Harmattan","HeadlandOne","Hedvig Letters Sans","Hedvig Letters Serif","Heebo","Henny Penny","Hepta Slab","Hermeneus One","Herr Von Muellerhoff","Hi Melody","Hina Mincho","Hind","Hind Colombo","Hind Guntur","Hind Jalandhar","Hind Kochi","Hind Madurai","Hind Mysuru","Hind Siliguri","Hind Vadodara","Holtwood One SC","Homemade Apple","Homenaje","Honk","Hubballi","Hurricane","IBM Plex Mono","IBM Plex Sans","IBM Plex Sans Condensed","IBM Plex Sans Devanagari","IBM Plex Sans Hebrew","IBM Plex Sans JP","IBM Plex Sans KR","IBM Plex Sans Thai","IBM Plex Sans Thai Looped","IBM Plex Serif","IM FELL DW Pica","IM FELL DW Pica SC","IM FELL Double Pica","IM FELL Double Pica SC","IM FELL English","IM FELL English SC","IM FELL French Canon","IM FELL French Canon SC","IM FELL Great Primer","IM FELL Great Primer SC","Ibarra Real Nova","Iceberg","Iceland","Imbue","Imperial Script","Imprima","Inclusive Sans","Inconsolata","Inder","Indie Flower","Ingrid Darling","Inika","Inknut Antiqua","Inria Sans","Inria Serif","Inspiration","Instrument Sans","Instrument Serif","Inter","Irish Grover","Island Moments","Istok Web","Italiana","Italianno","Itim","Jacquard 12","Jacquard 12 Charted","Jacquard 24","Jacquard 24 Charted","Jacquarda Bastarda 9","Jacquarda Bastarda 9 Charted","Jacques Francois","Jacques Francois Shadow","Jaini","Jaini Purva","Jaldi","Jaro","JejuGothic","JejuHallasan","JejuMyeongjo","Jersey 10","Jersey 10 Charted","Jersey 15","Jersey 15 Charted","Jersey 20","Jersey 20 Charted","Jersey 25","Jersey 25 Charted","JetBrains Mono","Jim Nightshade","Joan","Jockey One","Jolly Lodger","Jomhuria","Jomolhari","Josefin Sans","Josefin Slab","Jost","Joti One","Jua","Judson","Julee","Julius Sans One","Junge","Jura","Just Another Hand","Just Me Again Down Here","K2D","Kablammo","Kadwa","Kaisei Decol","Kaisei HarunoUmi","Kaisei Opti","Kaisei Tokumin","Kalam","Kalnia","Kalnia Glaze","Kameron","Kanit","Kantumruy","Kantumruy Pro","Kapakana","Karantina","Karla","Karma","Katibeh","Kaushan Script","Kavivanar","Kavoon","Kay Pho Du","Kdam Thmor","Kdam Thmor Pro","Keania One","Kelly Slab","Kenia","Khand","Khmer","Khula","Kings","Kirang Haerang","Kite One","Kiwi Maru","Klee One","Knewave","KoHo","KoPub Batang","Kodchasan","Kode Mono","Koh Santepheap","Kokoro","Kolker Brush","Konkhmer Sleokchher","Kosugi","Kosugi Maru","Kotta One","Koulen","Kranky","Kreon","Kristi","Krona One","Krub","Kufam","Kulim Park","Kumar One","Kumbh Sans","Kurale","Kyiv*Type Serif","Kyiv*Type Titling","KyivType Sans","LXGW WenKai Mono TC","LXGW WenKai TC","La Belle Aurore","Labrada","Lacquer","Laila","Lakki Reddy","Lalezar","Lancelot","Langar","Lao Muang Don","Lao Muang Khong","Lao Sans Pro","Lateef","Lato","Lavishly Yours","League Gothic","League Script","League Spartan","Leckerli One","Ledger","Lekton","Lemon","Lemonada","Lexend","Lexend Deca","Lexend Exa","Lexend Giga","Lexend Mega","Lexend Peta","Lexend Tera","Lexend Zetta","Libre Barcode 128","Libre Barcode 128 Text","Libre Barcode 39","Libre Barcode 39 Extended","Libre Barcode 39 Extended Text","Libre Barcode 39 Text","Libre Barcode EAN13 Text","Libre Baskerville","Libre Bodoni","Libre Caslon Display","Libre Caslon Text","Libre Franklin","Licorice","Life Savers","Ligconsolata","Lilita One","Lily Script One","Limelight","Linden Hill","Linefont","Lisu Bosa","Literata","Liu Jian Mao Cao","Livvic","Lobster","Lobster Two","Lohit Bengali","Lohit Devanagari","Lohit Tamil","Londrina Outline","Londrina Shadow","Londrina Sketch","Londrina Solid","Long Cang","Lora","Love Light","Love Ya Like A Sister","Loved by the King","Lovers Quarrel","Luckiest Guy","Lugrasimo","Lumanosimo","Lunasima","Lusitana","Lustria","Luxurious Roman","Luxurious Script","M PLUS 1","M PLUS 1 Code","M PLUS 1p","M PLUS 2","M PLUS Code Latin","Ma Shan Zheng","Macondo","Macondo Swash Caps","Mada","Madimi One","Magra","Maiden Orange","Maitree","Major Mono Display","Mako","Mali","Mallanna","Maname","Mandali","Manjari","Manrope","Mansalva","Manuale","Marcellus","Marcellus SC","Marck Script","Margarine","Marhey","Markazi Text","Marko One","Marmelad","Martel","Martel Sans","Martian Mono","Marvel","Mate","Mate SC","Material Icons","Maven Pro","McLaren","Mea Culpa"],
    ["Meddon","MedievalSharp","Medula One","Meera Inimai","Megrim","Meie Script","Meow Script","Merge One","Merienda","Merienda One","Merriweather","Merriweather Sans","Mervale Script","Metal","Metal Mania","Metamorphous","Metrophobic","Miama","Michroma","Micro 5","Micro 5 Charted","Milonga","Miltonian","Miltonian Tattoo","Mina","Mingzat","Miniver","Miriam Libre","Mirza","Miss Fajardose","Mitr","Mochiy Pop One","Mochiy Pop P One","Modak","Modern Antiqua","Mogra","Mohave","Moirai One","Molengo","Molle","Monda","Monofett","Monomaniac One","Monoton","Monsieur La Doulaise","Montaga","Montagu Slab","MonteCarlo","Montez","Montserrat","Montserrat Alternates","Montserrat Subrayada","Moo Lah Lah","Mooli","Moon Dance","Moul","Moulpali","Mountains of Christmas","Mouse Memoirs","Mplus 1p","Mplus 1p Bold","Mr Bedfort","Mr Dafoe","Mr De Haviland","Mrs Saint Delafield","Mrs Sheppards","Ms Madi","Mukta","Mukta Mahee","Mukta Malar","Mukta Vaani","Mulish","Murecho","MuseoModerno","My Soul","Myanmar Khyay","Myanmar Sans Pro","Mynerve","Mystery Quest","NATS","NTR","Nabla","Namdhinggo","Nanum Brush Script","Nanum Pen","NanumGothic","NanumGothicCoding","NanumMyeongjo","Narnoor","Neonderthaw","Nerko One","Neucha","Neuton","New Rocker","New Tegomin","News Cycle","Newsreader","Nico Moji","Niconne","Nikukyu","Niramit","Nixie One","Nobile","Nokora","Norican","Nosifer","Nosifer Caps","Notable","Nothing You Could Do","Noticia Text","Noto Color Emoji","Noto Color Emoji Compat Test","Noto Emoji","Noto Looped Thai","Noto Looped Thai UI","Noto Music","Noto Nastaliq Urdu","Noto Rashi Hebrew","Noto Sans","Noto Sans Arabic","Noto Sans Bengali","Noto Sans Bengali UI","Noto Sans Devanagari","Noto Sans Devanagari UI","Noto Sans Devanagari UI Condensed","Noto Sans Devanagari UI ExtraCondensed","Noto Sans Devanagari UI SemiCondensed","Noto Sans Georgian","Noto Sans Gujarati","Noto Sans Gujarati UI","Noto Sans HK","Noto Sans Hebrew","Noto Sans Hebrew Droid","Noto Sans Hebrew New","Noto Sans JP","Noto Sans Javanese","Noto Sans KR","Noto Sans Kannada","Noto Sans Kannada UI","Noto Sans Khmer","Noto Sans Lao","Noto Sans Lao Condensed","Noto Sans Lao ExtraCondensed","Noto Sans Lao SemiCondensed","Noto Sans Malayalam","Noto Sans Malayalam UI","Noto Sans Math","Noto Sans New Tai Lue","Noto Sans SC","Noto Sans Symbols","Noto Sans Symbols2","Noto Sans TC","Noto Sans Tai Le","Noto Sans Tai Tham","Noto Sans Tai Viet","Noto Sans Tamil","Noto Sans Tamil Supplement","Noto Sans Tamil UI","Noto Sans Telugu","Noto Sans Telugu UI","Noto Sans Thai","Noto Sans Thai UI","Noto Serif","Noto Serif Bengali","Noto Serif Gujarati","Noto Serif HK","Noto Serif JP","Noto Serif KR","Noto Serif Kannada","Noto Serif Malayalam","Noto Serif SC","Noto Serif TC","Noto Serif Tamil","Noto Serif Tamil Slanted","Noto Serif Telugu","Noto Serif Thai","Noto Traditional Nushu","Noto Znamenny Musical Notation","NotoSerifTamilSlanted","Nova Cut","Nova Flat","Nova Oval","Nova Round","Nova Script","Nova Slim","Nova Square","NovaMono","Numans","Nunito","Nunito Sans","Nuosu SIL","OFL Sorts Mill Goudy TT","Odibee Sans","Odor Mean Chey","OdorMeanChey","Offside","Oi","Ojuju","Old Standard TT","Oldenburg","Ole","Oleo Script","Oleo Script Swash Caps","Onest","Oooh Baby","Open Sans","Open Sans Condensed","Open Sans Hebrew","Open Sans Hebrew Condensed","Oranienbaum","Orbit","Orbitron","Oregano","Orelega One","Orienta","Original Surfer","Oswald","Otomanopee One","Outfit","Over the Rainbow","Overlock","Overlock SC","Overpass","Overpass Mono","Ovo","Oxanium","Oxygen","Oxygen Mono","PT Mono","PT Sans","PT Sans Caption","PT Sans Narrow","PT Serif","PT Serif Caption","Pacifico","Padauk","Padyakke Expanded One","Palanquin","Palanquin Dark","Palette Mosaic","Pangolin","Paprika","Parisienne","Passero One","Passion One","Passions Conflict","Pathway Extreme","Pathway Gothic One","Patrick Hand","Patrick Hand SC","Pattaya","Patua One","Pavanam","Paytone One","Pecita","Peddana","Peralta","Permanent Marker","Petemoss","Petit Formal Script","Petrona","Phetsarath","Philosopher","Phudu","Piazzolla","Piedra","Pinyon Script","Pirata One","Pixelify Sans","Plaster","Platypi","Play","Playball","Playfair","Playfair Display","Playfair Display SC","Playpen Sans","Playwrite AR","Playwrite AT","Playwrite AU NSW","Playwrite AU QLD","Playwrite AU SA","Playwrite AU TAS","Playwrite AU VIC","Playwrite BE VLG","Playwrite BE WAL","Playwrite BR","Playwrite CA","Playwrite CL","Playwrite CO","Playwrite CU","Playwrite CZ","Playwrite DE Grund","Playwrite DE LA","Playwrite DE SAS","Playwrite DE VA","Playwrite DK Loopet","Playwrite DK Uloopet","Playwrite ES","Playwrite ES Deco"],
    ["Playwrite FR Moderne","Playwrite FR Trad","Playwrite GB J","Playwrite GB S","Playwrite HR","Playwrite HR Lijeva","Playwrite HU","Playwrite ID","Playwrite IE","Playwrite IN","Playwrite IS","Playwrite IT Moderna","Playwrite IT Trad","Playwrite MX","Playwrite NG Modern","Playwrite NL","Playwrite NO","Playwrite NZ","Playwrite PE","Playwrite PL","Playwrite PT","Playwrite RO","Playwrite SK","Playwrite TZ","Playwrite US Modern","Playwrite US Trad","Playwrite VN","Playwrite ZA","Plus Jakarta Sans","Podkova","PoetsenOne","Poiret One","Poller One","Poltawski Nowy","Poly","Pompiere","Ponnala","Pontano Sans","Poor Story","Poppins","Port Lligat Sans","Port Lligat Slab","Porter Sans Block","Post No Bills Colombo","Post No Bills Colombo ExtraBold","Post No Bills Colombo Light","Post No Bills Colombo Medium","Post No Bills Colombo SemiBold","Post No Bills Jaffna","Post No Bills Jaffna ExtraBold","Post No Bills Jaffna Light","Post No Bills Jaffna Medium","Post No Bills Jaffna SemiBold","Potta One","Pragati Narrow","Praise","Prata","Preahvihear","Press Start 2P","Pridi","Princess Sofia","Prociono","Prompt","Prosto One","Protest Guerrilla","Protest Revolution","Protest Riot","Protest Strike","Proza Libre","Public Sans","Puppies Play","Puritan","Purple Purse","Qahiri","Quando","Quantico","Quattrocento","Quattrocento Sans","Questrial","Quicksand","Quintessential","Qwigley","Qwitcher Grypen","REM","RU Serius","Racing Sans One","Radio Canada","Radio Canada Big","Radley","Rajdhani","Rakkas","Raleway","Raleway Dots","Ramabhadra","Ramaraja","Rambla","Rammetto One","Rampart One","Ranchers","Rancho","Ranga","Rasa","Rationale","Ravi Prakash","Readex Pro","Recursive","Red Hat Display","Red Hat Mono","Red Hat Text","Red Rose","Redacted","Redacted Script","Reddit Mono","Reddit Sans","Reddit Sans Condensed","Redressed","Reem Kufi","Reem Kufi Fun","Reem Kufi Ink","Reenie Beanie","Reggae One","Rethink Sans","Revalia","Rhodium Libre","Ribeye","Ribeye Marrow","Righteous","Risque","Road Rage","Roboto","Roboto Condensed","Roboto Flex","Roboto Mono","Roboto Serif","Roboto Slab","Rochester","Rock 3D","Rock Salt","RocknRoll One","Rokkitt","Romanesco","Ropa Sans","Rosario","Rosarivo","Rouge Script","Rounded Mplus 1c","Rounded Mplus 1c Bold","Rowdies","Rozha One","Rubik","Rubik 80s Fade","Rubik Beastly","Rubik Broken Fax","Rubik Bubbles","Rubik Burned","Rubik Dirt","Rubik Distressed","Rubik Doodle Shadow","Rubik Doodle Triangles","Rubik Gemstones","Rubik Glitch","Rubik Glitch Pop","Rubik Iso","Rubik Lines","Rubik Maps","Rubik Marker Hatch","Rubik Maze","Rubik Microbe","Rubik Mono One","Rubik Moonrocks","Rubik One","Rubik Pixels","Rubik Puddles","Rubik Scribble","Rubik Spray Paint","Rubik Storm","Rubik Vinyl","Rubik Wet Paint","Ruda","Rufina","Ruge Boogie","Ruluko","Rum Raisin","Ruslan Display","Russo One","Ruthie","Ruwudu","Rye","SF Compact","SF Compact Rounded","SF Pro","SF Pro Rounded","STIX Two Math","STIX Two Text","Sacramento","Sahitya","Sail","Saira","Saira Condensed","Saira ExtraCondensed","Saira SemiCondensed","Saira Stencil One","Salsa","Sanchez","Sancreek","Sankofa Display","Sansation","Sansation Light","Sansita","Sansita One","Sansita Swashed","Sarabun","Sarala","Sarina","Sarpanch","Sassy Frass","Satisfy","Sawarabi Gothic","Sawarabi Mincho","Scada","Scheherazade","Scheherazade New","Schibsted Grotesk","Schoolbell","Scope One","Seaweed Script","Secular One","Sedan","Sedan SC","Sedgwick Ave","Sedgwick Ave Display","Sen","Send Flowers","SeoulHangang","SeoulHangang CB","SeoulHangang CBL","SeoulHangang CEB","SeoulHangang CL","SeoulHangang CM","SeoulNamsan","SeoulNamsan CB","SeoulNamsan CBL","SeoulNamsan CEB","SeoulNamsan CL","SeoulNamsan CM","Sevillana","Seymour One","Shadows Into Light","Shadows Into Light Two","Shalimar","Shantell Sans","Shanti","Share","Share Tech","Share Tech Mono","Shippori Antique","Shippori Antique B1","Shippori Mincho","Shippori Mincho B1","Shizuru","Shojumaru","Short Stack","Shrikhand","Siemreap","Sigmar","Sigmar One","Signika","Signika Negative","Signika Negative SC","Signika SC","Silkscreen","Simonetta","Single Day","Sintony","SirinStencil","Sitara","Six Caps","Sixtyfour","Skranji","Slabo 13px","Slabo 27px","Slackey","Slackside One","Smokum","Smooch","Smooch Sans","Smythe","Sniglet","Snippet","Snowburst One","Sofadi One","Sofia","Sofia Sans","Sofia Sans Condensed","Sofia Sans Extra Condensed","Sofia Sans Semi Condensed","Solitreo","Solway","Sometype Mono","Song Myung"],
    ["Sono","Sonsie One","Sora","Sorts Mill Goudy","Souliyo Unicode","Source Code Pro","Source Sans 3","Source Sans Pro","Source Serif 4","Source Serif Pro","Space Grotesk","Space Mono","Spartan","Special Elite","Spectral","Spectral SC","Spicy Rice","Spinnaker","Spirax","Splash","Spline Sans","Spline Sans Mono","Squada One","Square Peg","Sree Krushnadevaraya","Sriracha","Srisakdi","Staatliches","Stalemate","Stalinist One","Stardos Stencil","Stick","Stick No Bills","Stint Ultra Condensed","Stint Ultra Expanded","Stoke","Strait","Strong","Style Script","Stylish","Sudo Var","Sue Ellen Francisco","Suez One","Sulphur Point","Sumana","Sunflower","Sunshiney","Supermercado","Sura","Suranna","Suravaram","Suwannaphum","Swanky and Moo Moo","Syncopate","Syne","Syne Mono","Syne Tactile","Tac One","Tai Heritage Pro","Tajawal","Tangerine","Tapestry","Taprom","Tauri","Taviraj","Teachers","Teko","Tektur","Telex","Tenali Ramakrishna","Tenor Sans","Text Me One","Texturina","Thabit","TharLon","Thasadith","The Girl Next Door","The Nautigal","Tienne","Tillana","Tilt Neon","Tilt Prism","Tilt Warp","Timmana","Tinos","Tiny5","Tiro Bangla","Tiro Devanagari Hindi","Tiro Devanagari Marathi","Tiro Devanagari Sanskrit","Tiro Gurmukhi","Tiro Kannada","Tiro Tamil","Tiro Telugu","Titan One","Titillium Web","Tomorrow","Tourney","Trade Winds","Train One","Trirong","Trispace","Trocchi","Trochut","Truculenta","Trykker","Tsukimi Rounded","Tuffy","Tulpen One","Turret Road","Twinkle Star","Ubuntu","Ubuntu Condensed","Ubuntu Mono","Ubuntu Sans","Ubuntu Sans Mono","Uchen","Ultra","Unbounded","Uncial Antiqua","Underdog","Unica One","UnifrakturCook","UnifrakturMaguntia","Unkempt","Unlock","Unna","Updock","Urbanist","VT323","Vampiro One","Varela","Varela Round","Varta","Vast Shadow","Vazirmatn","Vesper Libre","Viaoda Libre","Vibes","Vibur","Victor Mono","Vidaloka","Viga","Vina Sans","Voces","Volkhov","Vollkorn","Vollkorn SC","Voltaire","Vujahday Script","Waiting for the Sunrise","Wallpoet","Walter Turncoat","Warnes","Water Brush","Waterfall","Wavefont","Wellfleet","Wendy One","Whisper","WindSong","Wire One","Wittgenstein","Wix Madefor Display","Wix Madefor Text","Work Sans","Workbench","Xanh Mono","Yaldevi","Yaldevi Colombo","Yaldevi Colombo ExtraLight","Yaldevi Colombo Light","Yaldevi Colombo Medium","Yaldevi Colombo SemiBold","Yanone Kaffeesatz","Yantramanav","Yarndings 12","Yarndings 12 Charted","Yarndings 20","Yarndings 20 Charted","Yatra One","Yellowtail","Yeon Sung","Yeseva One","Yesteryear","Yinmar","Yomogi","Young Serif","Yrsa","Ysabeau","Ysabeau Infant","Ysabeau Office","Ysabeau SC","Yuji Boku","Yuji Hentaigana Akari","Yuji Hentaigana Akebono","Yuji Mai","Yuji Syuku","Yusei Magic","ZCOOL KuaiLe","ZCOOL QingKe HuangYou","ZCOOL XiaoWei","Zain","Zen Antique","Zen Antique Soft","Zen Dots","Zen Kaku Gothic Antique","Zen Kaku Gothic New","Zen Kurenaido","Zen Loop","Zen Maru Gothic","Zen Old Mincho","Zen Tokyo Zoo","Zeyada","Zhi Mang Xing","Zilla Slab","Zilla Slab Highlight","jsMath-cmbx10","jsMath-cmex10","jsMath-cmmi10","jsMath-cmr10","jsMath-cmsy10","jsMath-cmti10"],
]


CHINESE_KEYWORDS = {
    "SC",
    "TC",
    "HK",
    "ZCOOL",
    "WenKai",
    "Long Cang",
    "Liu Jian Mao Cao",
    "Ma Shan Zheng",
    "XiaoWei",
    "QingKe",
    "KuaiLe",
}

CHINESE_FAMILIES = {
    "LXGW WenKai Mono TC",
    "LXGW WenKai TC",
    "Liu Jian Mao Cao",
    "Long Cang",
    "Ma Shan Zheng",
    "Noto Sans HK",
    "Noto Sans SC",
    "Noto Sans TC",
    "Noto Serif HK",
    "Noto Serif SC",
    "Noto Serif TC",
    "ZCOOL KuaiLe",
    "ZCOOL QingKe HuangYou",
    "ZCOOL XiaoWei",
    "Zhi Mang Xing",
}


def classify_family(family: str) -> tuple[str, str]:
    if family in CHINESE_FAMILIES:
        return "Chinese", "explicit_cjk_family"
    if any(keyword in family for keyword in CHINESE_KEYWORDS):
        return "Chinese", "name_keyword_match"
    return "English", "fallback_non_cjk_bucket"


def make_sheet_xml(rows: list[tuple[str, str, str]], tab_name: str) -> str:
    sheet_rows = [
        ('A1', 'font_family'),
        ('B1', 'tab'),
        ('C1', 'classification_reason'),
        ('D1', 'source'),
    ]
    for idx, (family, bucket, reason) in enumerate(rows, start=2):
        sheet_rows.extend(
            [
                (f'A{idx}', family),
                (f'B{idx}', tab_name),
                (f'C{idx}', reason),
                (f'D{idx}', 'Figma remote MCP listAvailableFontsAsync family list'),
            ]
        )
    cells = []
    current_row = 1
    row_cells: list[str] = []
    for ref, value in sheet_rows:
        row_num = int(''.join(ch for ch in ref if ch.isdigit()))
        if row_num != current_row:
            cells.append(f'<row r="{current_row}">{"".join(row_cells)}</row>')
            row_cells = []
            current_row = row_num
        row_cells.append(
            f'<c r="{ref}" t="inlineStr"><is><t>{escape(value)}</t></is></c>'
        )
    cells.append(f'<row r="{current_row}">{"".join(row_cells)}</row>')
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<sheetData>'
        + ''.join(cells)
        + '</sheetData></worksheet>'
    )


def build_workbook(output_path: Path, chinese_rows: list[tuple[str, str, str]], english_rows: list[tuple[str, str, str]]) -> None:
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>"""

    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>"""

    workbook = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Chinese" sheetId="1" r:id="rId1"/>
    <sheet name="English" sheetId="2" r:id="rId2"/>
  </sheets>
</workbook>"""

    workbook_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/>
</Relationships>"""

    app = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Codex</Application>
</Properties>"""

    core = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Figma Remote MCP Font List</dc:title>
  <dc:creator>Codex</dc:creator>
</cp:coreProperties>"""

    with ZipFile(output_path, "w", ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", rels)
        zf.writestr("xl/workbook.xml", workbook)
        zf.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
        zf.writestr("xl/worksheets/sheet1.xml", make_sheet_xml(chinese_rows, "Chinese"))
        zf.writestr("xl/worksheets/sheet2.xml", make_sheet_xml(english_rows, "English"))
        zf.writestr("docProps/app.xml", app)
        zf.writestr("docProps/core.xml", core)


def main() -> None:
    families: list[str] = []
    seen: set[str] = set()
    for page in PAGES:
        for family in page:
            if family not in seen:
                seen.add(family)
                families.append(family)

    chinese_rows: list[tuple[str, str, str]] = []
    english_rows: list[tuple[str, str, str]] = []
    for family in families:
        bucket, reason = classify_family(family)
        row = (family, bucket, reason)
        if bucket == "Chinese":
            chinese_rows.append(row)
        else:
            english_rows.append(row)

    output_path = Path("fonts") / "figma-remote-fontlist-tabs.xlsx"
    build_workbook(output_path, chinese_rows, english_rows)

    print(f"families={len(families)}")
    print(f"chinese={len(chinese_rows)}")
    print(f"english={len(english_rows)}")
    print(output_path.resolve())


if __name__ == "__main__":
    main()
