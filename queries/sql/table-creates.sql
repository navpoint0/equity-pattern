-- Table: equities.index_data

-- DROP TABLE equities.index_data;

CREATE TABLE equities.index_data
(
  date date NOT NULL,
  nasdaq_change real NOT NULL,
  spy_change real NOT NULL,
  djia_change real NOT NULL,
  id serial NOT NULL,
  CONSTRAINT index_data_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE equities.index_data OWNER TO postgres;

-- Table: equities.index_data

-- DROP TABLE equities.index_data;

CREATE TABLE equities.index_data
(
  date date NOT NULL,
  nasdaq_change real NOT NULL,
  spy_change real NOT NULL,
  djia_change real NOT NULL,
  id serial NOT NULL,
  CONSTRAINT index_data_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE equities.index_data OWNER TO postgres;

-- Table: equities.stock_master

-- DROP TABLE equities.stock_master;

CREATE TABLE equities.stock_master
(
  ticker character varying(5) NOT NULL,
  tracking_date date NOT NULL,
  initial_direction character(1) NOT NULL,
  reason character varying(20),
  "index" character varying(6) NOT NULL,
  id serial NOT NULL,
  CONSTRAINT stock_master_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE equities.stock_master OWNER TO postgres;
