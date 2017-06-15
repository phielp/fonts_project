# Read in the csvs. You can choose wherever you have saved them
Phoible <- read.csv(file.choose(), sep=",", fileEncoding= "UTF-8", header = TRUE) 
Segments <- read.csv(file.choose(), sep="\t", fileEncoding= "UTF-8", header = TRUE)

#PhoUni <- subset(Phoible, !duplicated(Phoneme))

# This bit basically just does a big dictionary lookup and grabs the phonological features for each of the segments, appending them as a new column
require(dplyr)
require(tidyr)
Segments$PhonFeats <- PhoUni[match(Segments$Substitute,PhoUni$Phoneme),]$PhonFeats

write.csv(Segments, file = 'segments_final.txt', fileEncoding = 'utf-8')
