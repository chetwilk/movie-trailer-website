import classic_movies
import media

# Use this template to add additonal movies.
# movie_title = media.Movie("Movie Title",
#                           "Storyline",
#                           "movie_poster_image_url",
#                           "movie_trailer_url")

# The following are instances of the the class Movie, found the file media.py 
my_man_godfrey = media.Movie("My Man Godfrey",
                          "Fifth Avenue socialite Irene Bullock (Carole Lombard) needs a 'forgotten man' to win a scavenger hunt, and no one is more forgotten than Godfrey Park (William Powell), who resides in a dump by the East River. Irene hires Godfrey as a servant for her riotously unhinged family, to the chagrin of her spoiled sister, Cornelia (Gail Patrick), who tries her best to get Godfrey fired. As Irene falls for her new butler, Godfrey turns the tables and teaches the frivolous Bullocks a lesson or two.",
                          "http://upload.wikimedia.org/wikipedia/en/6/62/My_man_godfrey.jpg",
                          "https://www.youtube.com/watch?v=6zkZd9GkxWc")
the_african_queen = media.Movie("The African Queen",
                          "After religious spinster's (Katharine Hepburn) missionary brother is killed in WWI Africa, dissolute steamer captain (Humphrey Bogart) offers her safe passage. She's not satisfied so she persuades him to destroy a German gunboat. The two spend most of their time fighting with each other rather than the Germans. Time alone on the river leads to love.",
                          "http://upload.wikimedia.org/wikipedia/en/2/2e/The-african-queen-1-.jpeg",
                          "https://www.youtube.com/watch?v=HUKpm2bcIz8")
the_maltese_falcon = media.Movie("The Maltese Falcon",
                          "In this noir classic, detective Sam Spade (Humphrey Bogart) gets more than he bargained for when he takes a case brought to him by a beautiful but secretive woman (Mary Astor). As soon as Miss Wonderly shows up, trouble follows as Sam's partner is murdered and Sam is accosted by a man (Peter Lorre) demanding he locate a valuable statuette. Sam, entangled in a dangerous web of crime and intrigue, soon realizes he must find the one thing they all seem to want: the bejeweled Maltese falcon.",
                          "http://upload.wikimedia.org/wikipedia/en/9/99/Falconm.JPG",
                          "https://www.youtube.com/watch?v=phUxnXGhEiI")
his_girl_friday = media.Movie("His Girl Friday",
                          "When hard-charging New York newspaper editor Walter Burns (Cary Grant) discovers that his ex-wife, investigative reporter Hildy Johnson (Rosalind Russell), has gotten engaged to milquetoast insurance agent Bruce Baldwin (Ralph Bellamy), he unsuccessfully tries to lure her away from tame domestic life with a story about the impending execution of convicted murderer Earl Williams. But when Hildy discovers Williams may be innocent, her reporter instincts take over.",
                          "http://upload.wikimedia.org/wikipedia/en/1/1a/His_Girl_Friday_poster.jpg",
                          "https://www.youtube.com/watch?v=dHVvnEWez1M")
its_a_wonderful_life = media.Movie("It's a Wonderful Life",
                          "After George Bailey (James Stewart) wishes he had never been born, an angel (Henry Travers) is sent to earth to make George's wish come true. George starts to realize how many lives he has changed and impacted, and how they would be different if he was never there.",
                          "http://upload.wikimedia.org/wikipedia/en/9/95/Its_A_Wonderful_Life_Movie_Poster.jpg",
                          "https://www.youtube.com/watch?v=LJfZaT8ncYk")
citizen_kane = media.Movie("Citizen Kane",
                          "When a reporter is assigned to decipher newspaper magnate Charles Foster Kane's (Orson Welles) dying words, his investigation gradually reveals the fascinating portrait of a complex man who rose from obscurity to staggering heights. Though Kane's friend and colleague Jedediah Leland (Joseph Cotten), and his mistress, Susan Alexander (Dorothy Comingore), shed fragments of light on Kane's life, the reporter fears he may never penetrate the mystery of the elusive man's final word, 'Rosebud.'",
                          "http://upload.wikimedia.org/wikipedia/en/c/ce/Citizenkane.jpg",
                          "https://www.youtube.com/watch?v=zyv19bg0scg")
the_wizard_of_oz = media.Movie("The Wizard of Oz",
                          "When a tornado rips through Kansas, Dorothy (Judy Garland) and her dog, Toto, are whisked away in their house to the magical land of Oz. They follow the Yellow Brick Road toward the Emerald City to meet the Wizard, and en route they meet a Scarecrow (Ray Bolger) that needs a brain, a Tin Man (Jack Haley) missing a heart, and a Cowardly Lion (Bert Lahr) who wants courage. The wizard asks the group to bring him the broom of the Wicked Witch of the West (Margaret Hamilton) to earn his help.",
                          "http://upload.wikimedia.org/wikipedia/commons/c/ca/WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg",
                          "https://www.youtube.com/watch?v=vkZcYMy85lY")
casablanca = media.Movie("Casablanca",
                          "Rick Blaine (Humphrey Bogart), who owns a nightclub in Casablanca, discovers his old flame Ilsa (Ingrid Bergman) is in town with her husband, Victor Laszlo (Paul Henreid). Laszlo is a famed rebel, and with Germans on his tail, Ilsa knows Rick can help them get out of the country.",
                          "http://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",
                          "https://www.youtube.com/watch?v=BZtWRRa_8I0")
gone_with_the_wind = media.Movie("Gone with the Wind",
                          "Epic Civil War drama focuses on the life of petulant southern belle Scarlett O'Hara (Vivien Leigh). Starting with her idyllic on a sprawling plantation, the film traces her survival through the tragic history of the South during the Civil War and Reconstruction, and her tangled love affairs with Ashley Wilkes (Leslie Howard) and Rhett Butler (Clark Gable).",
                          "http://upload.wikimedia.org/wikipedia/commons/2/27/Poster_-_Gone_With_the_Wind_01.jpg",
                          "https://www.youtube.com/watch?v=OFu-jemU-bA")

movies = [my_man_godfrey, the_african_queen, the_maltese_falcon, his_girl_friday, its_a_wonderful_life, citizen_kane, the_wizard_of_oz, casablanca, gone_with_the_wind]
classic_movies.open_movies_page(movies)