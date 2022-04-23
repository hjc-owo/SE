/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2022/4/9 20:26:26                            */
/*==============================================================*/


drop table if exists 习题;

drop table if exists 做题记录;

drop table if exists 学习课程;

drop table if exists 审核记录;

drop table if exists 用户;

drop table if exists 管理员;

drop table if exists 视频;

drop table if exists 认证证书;

drop table if exists 课程;

drop table if exists 错题集;

/*==============================================================*/
/* Table: 习题                                                    */
/*==============================================================*/
create table 习题
(
   习题ID                 int not null,
   课程ID                 int,
   用户ID                 int,
   题干内容                 text,
   参考答案                 text,
   primary key (习题ID)
);

/*==============================================================*/
/* Table: 做题记录                                                  */
/*==============================================================*/
create table 做题记录
(
   做题记录ID               int not null,
   习题ID                 int not null,
   错题集ID                int not null,
   是否正确                 bool,
   用户答案                 varchar(256),
   primary key (做题记录ID)
);

/*==============================================================*/
/* Table: 学习课程                                                  */
/*==============================================================*/
create table 学习课程
(
   用户ID                 int not null,
   课程ID                 int not null,
   primary key (用户ID, 课程ID)
);

/*==============================================================*/
/* Table: 审核记录                                                  */
/*==============================================================*/
create table 审核记录
(
   审核信息ID               int not null,
   管理员ID                int not null,
   审核日期                 datetime,
   审核结果                 int,
   审核视频ID               int,
   primary key (审核信息ID)
);

/*==============================================================*/
/* Table: 用户                                                    */
/*==============================================================*/
create table 用户
(
   用户ID                 int not null,
   用户名                  varchar(256),
   密码                   varchar(256),
   是否封禁                 bool,
   封禁截止时间               date,
   是否金牌讲师               bool,
   primary key (用户ID)
);

/*==============================================================*/
/* Table: 管理员                                                   */
/*==============================================================*/
create table 管理员
(
   管理员ID                int not null,
   管理员用户名               varchar(256),
   管理员密码                varchar(256),
   primary key (管理员ID)
);

/*==============================================================*/
/* Table: 视频                                                    */
/*==============================================================*/
create table 视频
(
   视频ID                 int not null,
   管理员ID                int,
   课程ID                 int,
   用户ID                 int,
   当日播放量                int,
   总播放量                 bigint,
   视频名称                 varchar(256),
   视频url                varchar(256),
   审核状态                 int,
   primary key (视频ID)
);

/*==============================================================*/
/* Table: 认证证书                                                  */
/*==============================================================*/
create table 认证证书
(
   学习完成日期               date,
   证书编号                 int not null,
   用户ID                 int not null,
   ASMART平台图标           longblob,
   primary key (证书编号)
);

/*==============================================================*/
/* Table: 课程                                                    */
/*==============================================================*/
create table 课程
(
   课程ID                 int not null,
   课程简介                 text,
   primary key (课程ID)
);

/*==============================================================*/
/* Table: 错题集                                                   */
/*==============================================================*/
create table 错题集
(
   错题集ID                int not null,
   用户ID                 int not null,
   primary key (错题集ID)
);

alter table 习题 add constraint FK_上传习题 foreign key (用户ID)
      references 用户 (用户ID) on delete restrict on update restrict;

alter table 习题 add constraint FK_含有习题 foreign key (课程ID)
      references 课程 (课程ID) on delete restrict on update restrict;

alter table 做题记录 add constraint FK_包含做题记录 foreign key (错题集ID)
      references 错题集 (错题集ID) on delete restrict on update restrict;

alter table 做题记录 add constraint FK_查看做题记录 foreign key (习题ID)
      references 习题 (习题ID) on delete restrict on update restrict;

alter table 学习课程 add constraint FK_学习课程 foreign key (用户ID)
      references 用户 (用户ID) on delete restrict on update restrict;

alter table 学习课程 add constraint FK_学习课程2 foreign key (课程ID)
      references 课程 (课程ID) on delete restrict on update restrict;

alter table 审核记录 add constraint FK_生成审核记录 foreign key (管理员ID)
      references 管理员 (管理员ID) on delete restrict on update restrict;

alter table 视频 add constraint FK_含有视频 foreign key (课程ID)
      references 课程 (课程ID) on delete restrict on update restrict;

alter table 视频 add constraint FK_用户上传视频 foreign key (用户ID)
      references 用户 (用户ID) on delete restrict on update restrict;

alter table 视频 add constraint FK_管理员上传视频 foreign key (管理员ID)
      references 管理员 (管理员ID) on delete restrict on update restrict;

alter table 认证证书 add constraint FK_获得认证证书 foreign key (用户ID)
      references 用户 (用户ID) on delete restrict on update restrict;

alter table 错题集 add constraint FK_创建错题集 foreign key (用户ID)
      references 用户 (用户ID) on delete restrict on update restrict;

