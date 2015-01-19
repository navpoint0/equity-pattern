-- Sequence: equities.index_data_id_seq

-- DROP SEQUENCE equities.index_data_id_seq;

CREATE SEQUENCE equities.index_data_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE equities.index_data_id_seq OWNER TO postgres;

-- Sequence: equities.stock_data_id_seq

-- DROP SEQUENCE equities.stock_data_id_seq;

CREATE SEQUENCE equities.stock_data_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 114
  CACHE 1;
ALTER TABLE equities.stock_data_id_seq OWNER TO postgres;

-- Sequence: equities.stock_master_id_seq

-- DROP SEQUENCE equities.stock_master_id_seq;

CREATE SEQUENCE equities.stock_master_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 39
  CACHE 1;
ALTER TABLE equities.stock_master_id_seq OWNER TO postgres;
