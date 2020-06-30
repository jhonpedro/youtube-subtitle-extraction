from youtube_transcript_api import YouTubeTranscriptApi
from nltk import pos_tag
from datetime import datetime
import functions

Api = YouTubeTranscriptApi


IdList = [
    "iFYWrDMfVNo",
    "YUeiAhpPMjQ",
    "XinLASYOJE4",
    "MOXLCjL4Ik4",
    "pMPlngyWHLM",
    "PQzUj5Hd0jk",
    "2vFQUw1JcGM",
    "shBkovJfWpk",
    "gisl6mK96Jg",
    "Y2EJfB9DMLU",
    "jtnLR8pA4YU",
    "YpHxxLAQCdk",
    "-9Nafr7zdJs",
    "ZdU4wMyiTSs",
    "ruOzUIA4rbs",
    "r7f-aR7vgg0",
    "SJzd9x2S2yg",
    "AdyGxhYWhoM",
    "pMPlngyWHLM",
    "qiGTRJlCnlA",
    "_HI7ltav9q4",
    "OJwzsL3of8k",
    "19IGAeoFKlU",
    "_PZldwo0vVo",
    "oSQfzjl110k",
    "jAzL4SE5-QM",
    "EGmlFdwD4C4",
    "7yBXNGVyN3Q",
    "WgYW2TMwA9U",
    "8qbqFsPov3g",
    "9N8yOMFgRdk",
    "DnHSTYuk-V4",
    "iphqkUNXxek",
    "mGLtyCOJe4A",
    "D5QvQmes198",
    "u5P_vryX0fo",
    "NctjqlfKC0U",
    "_Z-yaWEmV9c",
    "FcrMEfjLxwg"
]

#Name for the .csv file
option = input("Algorithm: ")
#First line of the table
csv = "Url;10 most spoken, times spoken;NoRepetition;WithRepetition;Ratio(NoRepetition/WithRepetition)\n"

filename = "test Planilha Algorithm"+ option +".csv"

option = int(option)

for Id in IdList:
    try:
        csv+= Id + ";"

        if option == 1:
            RawSubtitle = Api.get_transcript(Id, languages= ["pt"])

        if option == 2:
            ListSubtitles = Api.list_transcripts(Id)
            PtRawSubtitle = ListSubtitles.find_transcript(['pt'])
            SubtitleObject = PtRawSubtitle.translate('en')

            RawSubtitle = SubtitleObject.fetch()

        Subtitle = ""

        for phrase in RawSubtitle:
            Subtitle += phrase["text"] + " "

        Subtitle = functions.Format(Subtitle)

        if option == 1: 
            SubtitleSteemed = functions.Stemming(Subtitle)

            SubtitleSteemedNoStop = functions.RemoveStopWords(SubtitleSteemed)

            for wordRaw in functions.MoreSpoken(SubtitleSteemedNoStop):
                for word in Subtitle:
                    if(word.startswith(wordRaw[0])):
                        csv+= f"{word} {wordRaw[1]}, "
                        break

            SubtitleSteemedNoRep = sorted(set(SubtitleSteemed))

            csv+= ";"

            csv+= f"{len(SubtitleSteemedNoRep)};"
            csv+= f"{len(SubtitleSteemedNoStop)};"

            csv += f"{round(len(SubtitleSteemedNoRep)/len(SubtitleSteemedNoStop), 5)}\n"

        if option == 2:
            is_noun = lambda pos: pos[:2] == 'NN'
            nouns = [word for (word, pos) in pos_tag(Subtitle) if is_noun(pos)]


            nounsNoRep = sorted(set(nouns))

            nounsNoRepSteemed = functions.Steem(nounsNoRep)

            for SteemedNoun in functions.MoreSpoken(functions.Steem(nouns)):
                for noun in nouns:
                    if(noun.startswith(SteemedNoun[0])):
                        csv+= f"{noun} {SteemedNoun[1]}, "
                        break

            csv+= ";"

            csv+= f"{len(nounsNoRep)};"
            csv+= f"{len(nouns)};"

            csv += f"{round(len(nounsNoRep)/len(nouns), 5)}\n"
    except:
        print("Sem legendas para esse vídeo")
        csv += "No subtitle for this video\n"

f = open(filename, "w")

f.write(csv)

f.close()