from random import randint

def InterpretFileContents(FileName):
    """
    File contents will be of form
    Input1:1stPossibleResponse;2ndPossibleResponse;3rdPossibleResponse;etc...
    Input2:1stPossibleResponse;2ndPossibleResponse;3rdPossibleResponse;etc...
    """

    OutputDict = {}
    with open(FileName, "r") as ResponseFile:
        for Line in ResponseFile.readlines():
            Line.replace("\n", "")
            KeyString = Line.split(":")[0]
            ValueList = Line.split(":")[1].split(";")
            OutputDict[KeyString] = ValueList
    
    return OutputDict

def AppendToFile(FileName, InputString, OutputLst):
    with open(FileName, "a") as ResponseFile:
        TextToWrite = InputString + ":"
        for Output in OutputLst:
            TextToWrite += Output
            if Output != OutputLst[-1]:
                TextToWrite += ";"
            else:
                TextToWrite += "\n"
        ResponseFile.write(TextToWrite)

if __name__ == "__main__":
    ResponseDict = InterpretFileContents("Creative-Challenges/Responses.txt")
    ConvEnded = False
    if ConvEnded == False:
        UserInput = input("> ").lower()
        try:
            PossibleResponses = ResponseDict[UserInput]
            Output = PossibleResponses[randint(0, len(PossibleResponses) - 1)]
            print(Output)
        except KeyError:
            ## No response found
            NewResponseList = []
            MoreResponses = False
            while len(NewResponseList) == 0 or MoreResponses == True:
                MoreResponses = False
                NewResponseList.append(input("How should I answer that?\n> "))

                if input("Are there more responses to that phrase?\n> ").lower()[0] == "y":
                    MoreResponses = True
            
            AppendToFile("Responses,txt", UserInput, NewResponseList)
            ResponsesDict = InterpretFileContents("Responses.txt")

            