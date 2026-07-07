mkdir project
touch project1.txt
cp project1.txt project2.txt
mv project1.txt project2.txt
find . -name "project2.txt"

chmod 755 script.sh
tar -czvf project.tar.gz project/
mkdir extracted
tar -czvf project.tar.gz extracted project
tree
