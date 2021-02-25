#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

vector<vector<int> > graph;
vector<vector<int> > maze;
vector<bool> visited;
int N, M;

void BFS(int root){

  visited[root] = true;
  int cnt = 1;
  queue<pair<int,int> > q; //인덱스 저장
  pair<int, int> p = make_pair(root, 1);
  q.push(p);

  while(!q.empty()){

    int cur_idx = q.front().first;
    int cnt = q.front().second; q.pop(); //큐의 첫번째 요소부터 탐색시작

    if(cur_idx == N*M) {
      cout << cnt;
      return;
    }
    for(int i = 0; i<graph[cur_idx].size(); i++){
      //현재 인덱스에 연결된 모든 인덱스에 대해 방문 후 방문되었음을 표시
      int connected_idx = graph[cur_idx][i];
      if(!visited[connected_idx]){
        visited[connected_idx] = true;
        p = make_pair(connected_idx, cnt+1);
        q.push(p);
      }
    }
  }
  return;
}

int main(){

  scanf("%d %d", &N, &M);

  graph.resize(N*M + 1);
  visited.assign(N*M + 1, false);
  //create vector space of N * M
  maze.resize(N+1);
  for(int i = 1; i<=N; i++)
    maze[i].assign(M, -1);

  for(int i = 1; i<=N; i++){
    for(int j = 0; j<M; j++){
      int tmp;
      scanf("%1d", &tmp);
      if(tmp == 1) maze[i][j] = M * (i-1) + j + 1;
    }
  }

  for(int i = 1; i<=N; i++){
    for(int j = 0; j<M; j++){

      if(maze[i][j] != -1){
        if(i != 1)
          if(maze[i-1][j] != -1)
            graph[maze[i][j]].push_back(maze[i-1][j]);
        if(j != 0)
          if( maze[i][j-1] != -1)
            graph[maze[i][j]].push_back(maze[i][j-1]);
        if(i != N)
          if(maze[i+1][j] != -1)
            graph[maze[i][j]].push_back(maze[i+1][j]);
        if(j != M-1)
          if(maze[i][j+1] != -1)
            graph[maze[i][j]].push_back(maze[i][j+1]);
      }
    }
  }

  BFS(1);
}

