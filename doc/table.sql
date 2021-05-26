CREATE TABLE `company_detail` (
                                  `pid` varchar(32) NOT NULL,
                                  `basic_data` text COMMENT '基本信息',
                                  `directors_data` text COMMENT '主要人员信息',
                                  `branchs_data` text COMMENT '分支机构信息',
                                  `shareholders_data` text COMMENT '股东信息',
                                  `annual_report_data` text COMMENT '企业年报信息',
                                  `license` text COMMENT '行政许可',
                                  `abnormal` text COMMENT '经营异常名录',
                                  `change_record_data` text COMMENT '变更信息',
                                  `chattelmortgage` text COMMENT '动产抵押信息',
                                  `penalties` text COMMENT '行政处罚信息',
                                  `illegal` text COMMENT '列入严重违法名录信息',
                                  `equitypledge` text COMMENT '股权质押信息',
                                  `clearaccount` text COMMENT '清算信息',
                                  PRIMARY KEY (`pid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `company_summary` (
                                   `pid` varchar(32) NOT NULL,
                                   `ent_name` varchar(255) DEFAULT NULL COMMENT '公司名称',
                                   `ent_type` varchar(255) DEFAULT NULL COMMENT '企业类型',
                                   `domicile` varchar(255) DEFAULT NULL COMMENT '地址',
                                   PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;