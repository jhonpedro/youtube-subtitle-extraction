from youtube_transcript_api import YouTubeTranscriptApi
import functions

csvFile = open("Base profs csv.csv", encoding="utf-8")

dotCsv = str(csvFile.read())

csvFile.close()

LinkAndResources = []

dotCsv = dotCsv.split("\n")

dotCsv.pop(0)

for line in dotCsv:
    lineContent = line.split(";")
    LinkAndResources.append((lineContent[0], (lineContent[2].replace(" ", "").split(","))))

csv= "Url;Resource Types;Average Percentage\n"

for linkVideo, Resources in LinkAndResources:
    Id = linkVideo[-11:]
    csv += f"{linkVideo};"
    try:
        RawSubtitle = YouTubeTranscriptApi.get_transcript(Id, languages=["pt"])
        
        Subtitle = ""

        for phrase in RawSubtitle:
            Subtitle += phrase["text"] + " "
        
        Subtitle = functions.Format(Subtitle)

        Subtitle = functions.RemoveStopWords(Subtitle)        

        Subtitle = functions.Stemming(Subtitle)

        CountAparition = 0

        for resource in functions.Stemming(Resources):
            for word in Subtitle:
                if(resource == word):
                    CountAparition += 1
                    break
        for resource in Resources:
            csv += f"{resource}, "
        csv += ";"
        print(CountAparition/len(Resources))
        csv += f"{round((CountAparition/len(Resources)) * 100, 2) }\n"
    except:
        print("Deu erro")
        csv += f"No subtitles for this video;{0.0}\n"


f = open("Base profs csv calculado.csv", "w")

f.write(csv)

f.close()