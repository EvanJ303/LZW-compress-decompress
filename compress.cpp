#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
using namespace std;

//copy paste (will be deleted)

vector<int> encode(){
    std::map<string,int> encode_or_decode;
    for(int i=0;i<256;++i){
        encode_or_decode[string(1,char(i))]=i;
        std::cout << encode_or_decode[string(1,char(i))] << endl;
    }
    std::ifstream in("precompress.txt");
    char c;
    int table_count=0;
    std::string str_table_count=string(1,char(table_count));
    std::string current_str;
    std::string next_str;
    std::vector<int> result;

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

int main(){
    std::vector<int> encode_result=encode();
    ofstream out("aftercompress.txt");
    if(out.is_open()){
        for(int code:encode_result){
            out << code << " ";
        }
    }

    out.close();

    return 0;
}