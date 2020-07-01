from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path
import functions

# Need a file here
csvFile = open(Path("csv's/Recurso de aprendizagem todos.csv"), encoding="utf-8")

dotCsv = str(csvFile.read())

csvFile.close()

dotCsv = dotCsv.split("\n")

dotCsv.pop(0)

LinkAndResources = []
for line in dotCsv:
    aux = 0
    lineContent = line.split(";")
    for i in range(len(LinkAndResources)):
        if(LinkAndResources[i][0] == lineContent[1]):
            LineResources = lineContent[4].replace(" ", "").split(",")
            LinkResources = LinkAndResources[i][1]

            for linkResource in LinkResources:
                if (LineResources.count(linkResource) > 0):
                    LineResources.pop(LineResources.index(linkResource))
            for lineResources in LineResources:
                LinkResources.append(lineResources)
            
            LinkAndResources[i][1] = LinkResources
            aux+=1

    if(aux == 0):
        LinkAndResources.append([lineContent[1], lineContent[4].replace(" ", "").split(","), [], "0.0" ])

Percentages = []

for linkVideo, Resources, ResourcesInVideo, Percentage in LinkAndResources:
    Id = linkVideo[-11:]

    try:
        RawSubtitle = YouTubeTranscriptApi.get_transcript(Id, languages=["pt"])
        
        Subtitle = ""

        for phrase in RawSubtitle:
            Subtitle += phrase["text"] + " "
        
        Subtitle = functions.Format(Subtitle)

        Subtitle = functions.RemoveStopWords(Subtitle)        

        Subtitle = functions.Stemming(Subtitle)
        
        RawResources = [
                "avaliação",
                "declaração",
                "definição",
                "demonstração",
                "diagrama",
                "exemplo",
                "exercício",
                "experiência",
                "introdução",
                "narrativa",
                "palestra",
                "problema",
                "prova",
                "questionário",
                "resumo",
                "simulação",
                "slide",
                "tabela",
                "texto",
                "visão geral",
            ]

        for i, resource in enumerate(functions.Stemming(RawResources)):
            if (Subtitle.count(resource) > 0):
                ResourcesInVideo.append(RawResources[i])
                continue

        CountAparition = 0

        for resource in functions.Stemming(Resources):
            for word in Subtitle:
                if(resource == word):
                    CountAparition += 1
                    break
        
        Percentage = str(round((CountAparition/len(Resources)) * 100, 2))
        Percentages.append(str(round((CountAparition/len(Resources)) * 100, 2)))
        print(Percentage)
    except:
        print("Vídeo:", linkVideo )
        ResourcesInVideo.append(f"No subtitles for this video")
        Percentages.append("0")
        Percentage = 0

csv = "url;resources;resources_in_the_video;percentage of hit\n"

for i in range(len(LinkAndResources)):
    csv+=f"{LinkAndResources[i][0]};{LinkAndResources[i][1]};{LinkAndResources[i][2]};{Percentages[i]} \n"

f = open(Path("csv's/Recurso de aprendizagem todos calculado.csv"), "w")

f.write(csv)

f.close()