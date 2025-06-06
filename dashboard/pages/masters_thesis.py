import streamlit as st
import altair as alt
import streamlit.components.v1 as components

# This must be the first Streamlit command
st.set_page_config(
    page_title="Seeking Truth in A Time of War",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .block-container { padding-top: 0rem; }
    .stApp { background-color: #000; }
    h1, h2, h3, h4, h5, h6, p, div, span { color: #FAFAFA !important; }
    .css-6qob1r { background-color: #111 !important; }
    header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# App content
st.title("Seeking Truth in A Time of War")
st.markdown(
    """
    <style>
        /* Sidebar background to black */
        section[data-testid="stSidebar"] {
            background-color: black;
        }

        /* Sidebar text color to white */
        section[data-testid="stSidebar"] * {
            color: white;
        }

        /* Main content background to white */
        .main {
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Main content
st.write("In Jehad al-Saftawi’s final year of trying to flee Gaza for a new life in the United States, sheer desperation consumed him. He even fleetingly entertained the impulsive idea of running to the Israel border. As a photographer and journalist, he no longer wanted to exist in a place without a free press and where danger and suspicions were ever-present.")
st.text("")
st.write("Al-Saftawi is the son of a jihadist who belonged to one of the leading armed factions in Gaza, but he viewed the world through a far different lens than his father. He condemned the killing of innocent people on both sides of a centuries-old conflict and longed to leave behind the pain and hopelessness he felt.")
st.text("")
st.write("“Everything started to feel really burdensome and growing up with all of these different political beliefs I had,” he said. “I started feeling caged up and really wanted to just leave Gaza for no reason but personal survival.”")
st.text("")
st.write("How can humans organize themselves this vastly apart from one another? he wondered.")
st.text("")
st.write("After three rejections from Israeli security, al-Saftawi was allowed to cross the border in 2016 for an interview at the U.S. Consulate connected to his visa application. He had heard stories of Palestinians who dared to cross into Israel only to be captured by the army, but he was willing to take almost any risk.")
st.text("")
st.write("The nearly two-hour taxi ride to the Consulate provided time to reflect on his childhood in Gaza and Syria, and the aspirations he had as a boy. A strange yet familiar feeling also came over the 25-year-old: the last time he stepped foot in Israel, he was 14 years old and was there to visit his father at Ramon Prison. Al-Saftawi looked out at the homes that dotted the landscape, noting with a critical eye their prosperity compared to neighborhoods he knew in Gaza.")
st.text("")
st.write("As the taxi drove up to the Consulate’s roundabout, a group of his Israeli friends waited outside to embrace him. This was a surreal experience for him, breathing in the same air that was Gaza, and yet he felt worlds apart.")
st.text("")
st.write("Al-Saftawi caught his breath before stepping inside to join a queue. The person in front of him was an Israeli citizen also trying to emigrate to the United States. He reflected on their differences and, at this moment, their similarities.")
st.text("")
st.write("“Do you want to go to Al-Aqsa Mosque?” his friend, Athir, inquired after the interview.")
st.text("")
st.write("“No, I don’t want to do anything with this contentious place,” al-Saftawi replied.")
st.text("")
st.write("They rested under trees in the periphery of the Consulate. Al-Saftawi felt as though everyone was looking at him like an outsider, feeling sad for him. But if they looked closer, they could see the hope in his eyes. Leaving Gaza was more tangible now than ever.")
st.text("")
st.write("“I don’t want to go back,” he said, crying.")
st.text("")
st.write("Later that afternoon, Athir drove him to the Gaza border, where al-Saftawi crossed into his homeland and waited anxiously for another two months to receive approval from the Consulate. When word came, he and his wife, Lara Aburamadan, had just 72 hours to leave Gaza, beginning a dangerous journey that took them through Egypt for a flight to New York.")
st.text("")
st.write("The day of their departure was filled with excitement and tragedy. It was 1 a.m. Hundreds of people slept on the cold floor in the Egyptian Hall, their bags packed beside them. When their name was called out over the loudspeakers, their hearts began to race.  A flicker of hope was ignited as they were one step closer to a new life.")
st.text("")
st.write("Al-Saftawi and Aburamadan waited outside a shack to meet with a high-ranking officer.  The officer held their fate in his hands. He would determine whether they would survive by fleeing to America.")
st.text("")
st.write("“Just send me back to Gaza,” an elderly man, barely able to walk, shouted at an Egyptian officer as he left the shack. “I don’t want to go to your country.”")
st.text("")
st.write("Even though he was not going to Egypt, the man still had to gain permission to return to Gaza. As soon as al-Saftawi and Aburamadan entered the room, the high-ranking officer looked over their passports and other documents. It became clear by the officer’s kind demeanor that al-Saftawi and his wife paid money to get on the list to get out of Gaza.")
st.text("")
st.write("The border opened only a couple days throughout the year. It was a war zone at the time as ISIS was fighting with Egypt in Sinai, a peninsula in the country. Al-Saftawi paid $5,000 to get on a list otherwise it would have been years before their escape.")
st.text("")
st.write("After they left his office, al-Saftawi and Aburamadan went back to sleeping on the floor with the others.")
st.text("")
st.write("He thought to himself the promise they made to cross the border for Gaza to Egypt is finally coming into fruition, the escape is near.")
st.text("")
st.write("The trip to the Cairo airport almost felt never ending as they drove through a war zone in Sinai. Before arriving at the dozens of checkpoints, they slowed down due to ISIS raids on the Egyptian army. ISIS militants would blow themselves up or take over the checkpoint by use of force with machine guns.")
st.text("")
st.write("Eventually, they moved to Berkeley in the San Francisco Bay Area, where they continued to navigate the asylum process – and where, in October 2023, the long tail of the Israel-Palestine conflict disrupted their lives as visual storytellers.")
st.text("")
st.write("Growing up in Gaza, al-Saftawi lived with his mother and siblings on the fifth floor of a high-rise building owned by his uncle. Growing up in a neighborhood bearing his family’s name, his childhood was defined by violence and bloodshed as Israeli airstrikes caused destruction for miles.")
st.text("")
st.write("“The more I became politically aware of this place and its actors, the more I realized how normalized many things were in the eyes of Gazans,” he said during a series of recent interviews at the Berkeley apartment he and Aburamadan share.")
st.text("")
st.write("The Islamic term “ribat” was a concept that he was taught as a child. It is the idea that soldiers protect a fortress from the enemy. The practice of ribat took place every night in civilian neighborhoods of Gaza where street corners were filled with masked militants with guns drawn. Ribat became normalized in the consciousness of Gazans,  al-Saftawi said, adding that he was conditioned to think that Israelis were privileged while Gazans faced utter devastation and turmoil.")
st.text("")
st.write("He was drawn to cameras, not guns, and photography redefined the way he viewed the Israel-Palestine conflict. He never questioned what was happening around him, until he captured horrific atrocities on film.")
st.text("")
st.write("In 2012, Israel launched an eight-day air and ground offensive called Operation Pillar of Defense, which resulted in the death of Ahmed al-Jabari, the military commander of Hamas. More than 80 civilians were also killed.  In the immediate aftermath, the streets were desolate as civilians stayed inside to avoid becoming targets. Suddenly, al-Saftawi heard the sounds of chaos echoing from afar. He stood with others watching, anticipating what was coming.")
st.text("")
st.write("Hamas militants approached on motorcycles, cheering loudly as they dragged behind a body. Al-Saftawi started to film the incident, until a militant put a gun to his head shouting at him to delete the images. He later learned that the militants toured other streets in Gaza to showcase the body. Not long after, he decided to pursue journalism as a career. He wanted to document not only the fighting but also everyday life in Gaza.")
st.text("")
st.write("“The idea of leaving Gaza, it just was always there, not for the sake of accomplishment, but it was literally just personal survival because of personal freedom, political freedoms,” al-Saftawi said. Escaping the turmoil and bloodshed was not going to be easy, but he was determined to survive.")
st.text("")
st.write("In 2013, he discovered that Hamas had built tunnels under a house that his mother and sister were about to move into. One day their soon-to-be neighbor, Um Yazid Salha, asked his mother why al-Saftawi and his brother Hamza came to the house after midnight.  Salha reported witnessing a transport vehicle that would load and unload items.")
st.text("")
st.write("His mother was alarmed. She knew that al-Saftawi and his brother were not the source of this late-night activity. Every time they visited her, they’d leave around 10 p.m. and the family residence would be locked.")
st.text("")
st.write("The next day, al-Saftawi inspected the construction site along with his mother and brother, digging about half a meter deep until they hit a metal gate secured with a lock. Al-Saftawi was shocked – unsure why his family had become a target, especially since his father had longstanding ties with Hamas.")
st.text("")
st.write("He met with a masked militant who assured al-Saftawi that the tunnels had to be built to supply weapons for Hamas. The militant said they would later notify the family once the tunnels were removed. Oddly, some of the men who built the tunnels attended the same mosque as al-Saftawi.")
st.text("")
st.write("“We absolutely rejected having them continue to build and they told us, if you don’t wish to have it, we’ll remove it,” al-Saftawi said.")
st.text("")
st.write("Later that year, Hamza and al-Saftawi dug once more, expecting to find the tunnels gone. They were met with a large concrete slab, and his mother and her neighbors would continue to hear sounds of digging for years.")
st.text("")
st.write("Al-Saftawi felt a sense of shame for not talking about the tunnels with others, as his family was terrified about its repercussions. He later shared this story in Time magazine when he moved to Berkeley with Aburamadan.")
st.text("")
st.write("Aburamadan began to take photos of their new surroundings after the couple moved to the San Francisco Bay Area in 2017. She had used the hashtag #RefugeeEye when posting her photography on Instagram from Gaza, and now she planned to carry it forward in the U.S.")
st.text("")
st.write("Her photography included Abu Abed Attar, holding his son on his balcony at home in the Gaza strip. Attar was a Syrian refugee who had fled to Gaza in search of a better life. Other photos included a Palestinian woman during the Israeli war on Gaza holding her granddaughter.")
st.text("")
st.write("Aburamadan and al-Saftawi created Refugee Eye, a storytelling project that aimed to view the world from refugees' perspectives through photographs. They opened an art gallery on Valencia Street in San Francisco in March 2022, showcasing al-Saftawi’s exhibition titled “My Gaza: A City in Photographs.”")
st.text("")
st.write("The vivid images depicted Gaza residents evacuating during a ceasefire to children playing soccer in the deserted street. This exhibition allowed people to see what life was like in Gaza, the hardship he faced and why he needed a ticket out of “this prison,” he said.")
st.text("")
st.write("On Feb. 13, 2024, Time published his essay under the headline “Hamas Built Tunnels Beneath My Family’s Home in Gaza. Now It Lies in Ruin.” The article appeared in the midst of fierce protests across the U.S. following the Oct. 7, 2023, Hamas attack that killed about 1,200 people, most of them civilians, and led to more than 250 hostages being taken.")
st.text("")
st.write("Soon after, al-Saftawi received social media death threats and online harassment. One X user commented, “Release the hostages.”")
st.text("")
st.write("Other photographers and artists connected to the Refugee Eye gallery also received threats. Al-Saftawi thought it was ironic that many Americans who had never been to Gaza were harassing him for a detailed account from someone who was raised there. Although he had escaped Gaza, his past continued to follow him.")
st.text("")
st.write("Due to financial struggles Refugee Eye shut down in 2024 and has not reopened.")
st.text("")
st.write("Coming to the U.S. has shaped al-Saftawi’s understanding of how people view the Middle East conflict from a world apart. Some people in the Bay Area called artists connected to Refugee Eye telling them not to collaborate with the storytelling project, according to al-Saftawi.")
st.text("")
st.write("By then, al-Saftawi had learned that his mother’s home in Gaza, the property under which Hamas built tunnels, was destroyed due to the conflict.")
st.text("")
st.write("Although al-Saftawi has suffered backlash from Refugee Eye, he considers Berkeley his  home now.  He hopes to return to Gaza one day, but is unsure when that will be.")

# Enable Altair dark theme
alt.themes.enable("dark")