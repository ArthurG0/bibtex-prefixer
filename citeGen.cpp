#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//first parameter - name of the file to read into. second parameter - name of the file to run to.
int main(int argc, char** argv){
	ifstream ifs;
	ofstream w;
	string line;
	int count = 0;
	string res = "";

	ifs.open(argv[1]);
	w.open(argv[2]);

	if(ifs.fail()){
		cerr << "file doesn't exist" << endl;
		exit(1);
	}

	while(true){
		getline(ifs,line);
		if(ifs.eof()) break;
		if(line[0] == '@'){
			count++;
			string tmp = line.substr(line.find("{"));
			tmp = tmp.substr(1, tmp.size()-3);
			res += "~\\cite{" + tmp + "}\n";
		}

	}
	w << res;
	w << "Total citations: " << count << endl;

	ifs.close();
	w.close();


	return 0;



}
