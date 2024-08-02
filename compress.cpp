#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
using namespace std;

map<string,int> encode_or_decode;
string input_path;
string output_path;

vector<int> encode(){
    for(int i=0;i<256;++i){
        encode_or_decode[string(1,char(i))]=i;
        cout << "init map val " << encode_or_decode[string(1,char(i))] << endl;
    }
    ifstream in(input_path);
    char c;
    string current_str;
    string next_str;
    vector<int> result;

    if(in.is_open()){
        while(in.get(c)){
            next_str=current_str + string(1,c);
            if(encode_or_decode.count(next_str)){
                current_str=next_str;
            }
            else{
                result.push_back(encode_or_decode[current_str]);
                encode_or_decode[next_str]=encode_or_decode.size();
                current_str=string(1,c);
            }
        }
        if(!current_str.empty()){
            result.push_back(encode_or_decode[current_str]);
        }
    }

    in.close();

    return result;
}

void take_inputs(){
    cout << "INPUT PATH OF FILE TO BE COMPRESSED" << endl;
    cin >> input_path;
    cout << "INPUT FILE TO WRITE COMPRESSED DATA TO" << endl;
    cin >> output_path;
}

int main(){
    take_inputs();
    vector<int> encode_result=encode();
    ofstream out(output_path);
    if(out.is_open()){
        out << encode_or_decode.size()-256 << endl;
        for(auto values:encode_or_decode){
            if(values.second>255){
                out << values.first << " " << values.second << endl;
            }
        }
        for(int code:encode_result){
            out << code << " ";
        }
    }

    out.close();

    return 0;
}