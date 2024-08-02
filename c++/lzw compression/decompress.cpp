#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
using namespace std;

map <int,string> interpreted_map;
vector <string> decompressed_dat;
string input_path;
string output_path;

void prime_dictionary(){
    for(int i=0;i<256;++i){
        interpreted_map[i]=string(1,char(i));
        cout << interpreted_map[i] << endl;
    }
    ifstream in(input_path);
    int strmap_len;
    string s_val;
    int s_key;
    in >> strmap_len;
    for(int i=0;i<strmap_len;i++){
        in >> s_val;
        in >> s_key;
        interpreted_map[s_key]=s_val;
    }
    in.close();
}

void read_to_vector(){
    ifstream in(input_path);
    int strmap_len;
    string s_val;
    int s_key;
    in >> strmap_len;
    for(int i=0;i<strmap_len;i++){
        in >> s_val;
        in >> s_key;
    }
    int iterate_str;
    while(in >> iterate_str){
        decompressed_dat.push_back(interpreted_map[iterate_str]);
    }
    in.close();
}

void output_resu(){
    ofstream out(output_path);
    for(string code:decompressed_dat){
        out << code;
    }
    out.close();
}

void take_inputs(){
    cout << "INPUT PATH OF FILE TO BE DECOMPRESSED" << endl;
    cin >> input_path;
    cout << "INPUT FILE TO WRITE DECOMPRESSED DATA TO" << endl;
    cin >> output_path;
}

int main(){
    take_inputs();
    prime_dictionary();
    read_to_vector();
    output_resu();

    return 0;
}