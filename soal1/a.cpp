#include<bits/stdc++.h>
using namespace std;
int n;
int pout;
string string_;
bool used_number[16400]={};

int make_number(int i,int j){
	int  r=0;
	for(int t=i;t<=j;t++){
		if(string_[t]=='0')r=r*2;
		else r=r*2+1;
	}
	return r;
}

bool fun(int in){
	//cout<<string_<<endl;;
	int l=string_.size();
	if(l==pout){
		//cout<<"hello"<<endl;
		return true;
	}
	int new_num=make_number(l-1-(n-2),l-1);
	new_num=new_num*2+1;
	if(used_number[new_num]==0){
		string_+="1";
		used_number[new_num]=1;
		return fun(n);
	}
	else{
		//int new_num=make_number(l-1-(n-2),l-1);
		new_num--;		
		if(used_number[new_num]==0){
			string_+="0";
			used_number[new_num]=1;//.append(new_int)
			return fun(n);
		}
	}
	return false;
}
int checker(){
	if(pow(2,n)!=string_.size())
		return 0;
	
	string_=string_+string_;
	for(int i=0;i<pout;i++)used_number[i]=0;
	for(int i=0;i<pout;i++){
		int l=make_number(i,i+n-1);
		used_number[l]=1;
	}
	int z=1;
	for(int i=0;i<pout;i++)if(used_number[i]==0)z-=1;
	return max(0,z);
}
int main(){
	
	cin>>n;
	pout=pow(2,n);
	for(int i=0;i<n-1;i++)string_+='0';
	for(int i=0;i<pout;i++)used_number[i]=0;
	fun(n);
	cout<<string_<<endl<<string_.size()<<endl;
	cout<<checker();
}

