#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
queue<pair<int, int>> q;
int table[27][27];
bool visit[27][27]; 
int result[700];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,1,-1 };
int main() {
    int N;
    scanf("%d", &N);
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            scanf("%1d", &table[i][j]);
        }
    }
    int ret = 0; int x, y; int tx, ty;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (table[i][j] == 1 && visit[i][j]==false) {
                q.push(make_pair(i, j));
                result[ret]++;
                while (!q.empty()) {
                    y = q.front().first;
                    x = q.front().second;
                    visit[y][x] = true;
                    q.pop();
                    for (int i = 0; i < 4; i++) {
                        tx = x + dx[i];
                        ty = y + dy[i];
    if (tx >= 1 && ty >= 1 && tx <= N&&ty <= N&&visit[ty][tx] == false && table[ty][tx]==1) {
                            result[ret]++;
                            visit[ty][tx] = true;
                            q.push(make_pair(ty, tx));
                        }
                    }
                }
                ret++;
            }
        }
    }
 
    printf("%d\n", ret);
    std::sort(result , result + ret );
    for (int i = 0; i < ret; i++) {
        printf("%d\n", result[i]);
    }
}


