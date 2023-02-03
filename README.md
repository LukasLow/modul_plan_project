# Uni Goe Moduleplaner

This is my project to make the Moduleverzeichnis file in a clean Web interface that is easier to user than the regular one

## Roadmap

1. The first step is to read the Modulverzeichnis in the database
   1. separated every module from the Moduleverteichnis in an own PDF file (done)
   2. Extract and prepare the information for the database in variables
   3. set up the database for the modules
   4. loop thrue all files in ./single_Module and extract the wanted informations and save it in to the database
2. extract the Modulgruppen from Modulverzeichnis
3. Setup the webapp
   1. load the datebase and present it on localhost/
   2. develop a structerd way of showing every module