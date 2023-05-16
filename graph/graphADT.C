#ifndef HEADER_FILE
#define HEADER_FILE

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<malloc.h>
#define MAXV 15 // n 阶矩阵
#define SIDE 4 // 最大边数

// 邻接表储存
typedef struct ANode
{
int adjvex; // 该边邻接点编号
struct ANode *nextarc; // 指向下一条边的指针
}ArcNode;
typedef struct Vnode
{
ArcNode *firstarc; // 指向第一个边结点
}VNode; // 邻接表的头结点类型
typedef struct
{
VNode adjlist[MAXV]; // 邻接表的头结点数组
int n, e; // 图中的顶点数 n 和边数 e
}AdjGraph; // 完整的图邻接表类型

// 创建图的邻接表
void CreateAdj(AdjGraph *&G, int A[MAXV][MAXV], int n, int e)
{
int i,j; ArcNode *p;
G=(AdjGraph *)malloc(sizeof(AdjGraph));
for(i=0; i<n; i++) // 给邻接表中的所有头结点的指针域置初值
G->adjlist[i].firstarc=NULL;
for(i=0; i<n; i++) // 检查邻接矩阵 graph 中的每个元素
for(j=n-1; j>=0; j--)
if(A[i][j] != 0) // 存在一条边
// if(A[i][j] != 0 && A[i][j] != INF) // 存在一条边
{
p=(ArcNode *)malloc(sizeof(ArcNode)); // 创建一个结点
p->adjvex=j; // 存放邻结点
// p->weight=A[i][j]; // 存放权
p->nextarc=G->adjlist[i].firstarc; // 采用头结点插入法插入结点 p
G->adjlist[i].firstarc=p;
}
G->n=n;
G->e=e;
}

// 输出图
void DispAdj(AdjGraph *G)
{
int i; ArcNode *p;
for(i=0; i<G->n; i++)
{
p=G->adjlist[i].firstarc;
printf("%-2d: ", i);
while(p != NULL)
{
printf("%3d ->", p->adjvex);
// printf("%3d[%d]->", p->adjvex, p->weight);
p=p->nextarc;
}
printf(" NULL\n");
}
}

// 销毁邻接表
void DestroyAdj(AdjGraph *&G)
{
int i; ArcNode *pre, *p;
for(i=0; i<G->n; i++) // 扫描所有单链表
{
pre = G->adjlist[i].firstarc; // p 指向第 i 个单链表的头结点
if(pre != NULL)
{
p=pre->nextarc;
while(p!=NULL) // 释放第 i 个单链表的所有边结点
{
free(pre);
pre=p; p=p->nextarc;
}
free(pre);
}
}
free(G); // 释放头结点数组
}

// 生成二维数组
int graph[MAXV][MAXV]={0}; // 初始化全局 n 阶矩阵
int CreatGraph(int gc[MAXV][SIDE])
{
int i, j;
for(i=0; i<MAXV; i++)
{
for(j=0; j<SIDE; j++)
{
if(gc[i][j] != 0)
{
graph[i][gc[i][j]]=1; // 赋值为 1, 标记为两个顶点的边
graph[gc[i][j]][i]=1;
}
}
}
}

// 计算边数
int Sum(int gc[MAXV][SIDE])
{
int i=0, k=0, j;
for(; i<MAXV; i++)
{
for(j=0; j<SIDE; j++)
if(gc[i][j] != 0)
k++;
}
return k;
}

// 录入数组
int poss[MAXV]={0};
int posNum=0;
int GetArr()
{
int i=0, j=0, longer, num=0;
char ch[50];
printf("请输入顶点：");
gets(ch); // 获取输入字符串
// puts(ch); // 输出字符串
longer = strlen(ch);

// 解析出字符串中的数字 -- 数组实现
for(; i < longer ; i++)
{
while(ch[i] != ' ')
{
if((ch[i] >= '0') && (ch[i] <= '9'))
// 这里是用字符的ASCII码值进行比较，要减去0的ASCII码值即为实际的数字
num = num*10 + ch[i] - '0';

if(ch[i++] == '\0') break;
}
poss[j++] = num;
num=0;
}
// 必经顶点数
posNum=j;
poss[j]=-1;
// printf("%d", posNum);

// 输出 poss 数组
// for(i=0; poss[i] != -1; i++)
// printf("%d ", poss[i]);

}



#endif