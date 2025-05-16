define m = Character("Miniluv Officer", color="#c0c0c0")
define s = Character("Sophia (Sister)", color="#ff9999")
define n = Character("Neighbor", color="#66b3ff")
define p = Character("PROLES FEED ANNOUNCER", color="#ff4d4d")

image brutalist: 
    "brutalist-government-hallway.png"
    zoom 1.1

image apartment_img:
    "war_appartament.png"

image victory:
    "victory-mansion.png"

image street:
    "cobblestone-street.png"

image archive:
    "archive-room.png"

image living:
    "claustrophobic-living-room.png"

image prison:
    "prison-cell.png"

image poster:
    "poster.png"

image hospital:
    "hospital.png"

image country:
    "countryside.png"

default party_trust = 50
default family_safety = 50
default has_diary = False

label start:
    scene ministry_truth with fade
    show brutalist
    play music "dull_rumble.ogg" fadein 3.0

    "You adjust your armband bearing the emblem of the Thought Police, the cold fluorescent lights of the Ministry of Truth humming above."
    "Today's first assignment: review your own family's loyalty audit reports."

    m "Citizen. Your residential block shows irregular electricity usage. Explain."
    
    menu:
        "Report potential meter malfunction (Lie)":
            $ party_trust -= 10
            m "Doubtful. We'll inspect Sector 7 generators."
            
        "Blame neighbors (Divert suspicion)":
            $ party_trust += 5
            $ family_safety -= 15
            m "Noted. Two children were vaporized there last week. Efficient."
            
        "Request self-criticism session (Gain trust)":
            $ party_trust += 20
            $ family_safety -= 30
            "You spend three hours confessing imaginary faults while they monitor your sister's flat."

    scene sister_apartment with blinds
    show apartment_img
    show sister nervous at center
    play sound "telescreen_static.ogg"

    s "Brother! Thank Big Brother you're here. I... I made a terrible mistake."
    "Her eyes dart to the wall where fresh wallpaper partially covers chipped paint - a shape suspiciously resembling the letter 'F'."

    menu:
        "Demand immediate explanation":
            s "I tried writing... [she whispers] a poem. About real grass. Not the Victory Gin kind."
            $ has_diary = True
            
        "Check for listening devices first":
            $ family_safety += 15
            "You find a hidden microphone behind Marx's portrait. Crush it with your boot."
            s "I kept a diary. For two weeks. Burned it yesterday but..."
            
        "Slap her for emotional weakness":
            $ party_trust += 25
            $ family_safety = 0
            jump family_arrest

    "The telescreen flickers. Time is short."
    menu:
        "Order her to memorize 'Truth' pamphlets":
            $ family_safety += 10
            "She recites until her voice goes hoarse. The words mean nothing, but the rhythm pleases the microphones."
            
        "Plant false evidence in neighbor's flat":
            $ party_trust -= 20
            $ family_safety += 30
            "You slip contraband orange peels into Mrs. Whittaker's mailbox. She'll be dead by dawn."
            
        "Alter electricity records at Ministry":
            if party_trust > 40:
                $ party_trust -= 35
                $ family_safety += 40
                "You forge documents until 0400, hands stained with ink that'll never wash off."
            else:
                $ party_trust = 0
                jump ministry_discovery

    scene victory_mansion with dissolve
    play music "hymn.ogg" if_changed
    show street

    p "SPECIAL BULLETIN: HAPPINESS CAMPAIGN DOUBLES CHOCOLATE RATIONS TO 20 GRAMS!"
    "The announcement echoes through the cracked streets as you walk home. A rat darts over your sister's poem fragment in your pocket."


    if family_safety >= 60 and party_trust >= 40:
        jump golden_end
    elif family_safety <= 30:
        jump family_arrest
    elif party_trust <= 20:
        jump ministry_discovery
    else:
        jump uncertain_end

label family_arrest:
    scene cell with vpunch
    show prison
    show sister bloody at center

    s "Why didn't you let them take me sooner? Now they have you too."
    "The smell of burnt hair mixes with cheap disinfectant. Somewhere, a dial clicks to 101."
    jump game_over

label ministry_discovery:
    scene torture_chamber with fade
    show archive
    show officer at right

    m "We know about the altered reports. And your unnatural affection for... [spits] family."
    "They show you photos. You last exactly 9 minutes before naming everyone you've ever met."
    jump game_over

label golden_end:
    scene fields with fade
    show sister happy at center
    show countryside

    s "Is this... real sky?"
    "The prole smuggler takes your last gold teeth. You'll work the fields until the cough takes you, but her smile almost looks genuine."
    return

label uncertain_end:
    scene apartment with fade
    show sister neutral at center
    show living
    s "They transferred Mrs. Whittaker. New telescreen installed yesterday."
    "You nod, chewing your 20 grams of chocolate. It tastes like yesterday. It tastes like tomorrow."
    return

label game_over:
    play music "siren.ogg"
    scene big_brother with zoomin
    show poster
    "BIG BROTHER IS WATCHING"
    return