--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)

\c appraisal_db;

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: administrators; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.administrators (
    admin_id integer NOT NULL,
    is_active boolean,
    email character varying,
    is_verified boolean,
    password character varying,
    push_id character varying NOT NULL
);


--
-- Name: administrators_admin_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.administrators_admin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: administrators_admin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.administrators_admin_id_seq OWNED BY public.administrators.admin_id;


--
-- Name: staffs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.staffs (
    staff_id integer NOT NULL,
    first_name character varying NOT NULL,
    last_name character varying NOT NULL,
    other_name character varying,
    gender character varying,
    email character varying NOT NULL,
    supervisor_id integer,
    department character varying,
    grade integer,
    is_active boolean,
    is_superuser boolean,
    created_at date NOT NULL,
    updated_at date NOT NULL
);


--
-- Name: staffs_staff_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.staffs_staff_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: staffs_staff_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.staffs_staff_id_seq OWNED BY public.staffs.staff_id;


--
-- Name: user_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_type (
    usertype_id integer NOT NULL,
    title character varying
);


--
-- Name: user_type_usertype_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_type_usertype_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_type_usertype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_type_usertype_id_seq OWNED BY public.user_type.usertype_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying,
    hashed_password character varying,
    is_active boolean,
    is_superuser boolean,
    created_at date NOT NULL,
    updated_at date NOT NULL,
    reset_password_token character varying,
    staff_id integer
);


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: administrators admin_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrators ALTER COLUMN admin_id SET DEFAULT nextval('public.administrators_admin_id_seq'::regclass);


--
-- Name: staffs staff_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staffs ALTER COLUMN staff_id SET DEFAULT nextval('public.staffs_staff_id_seq'::regclass);


--
-- Name: user_type usertype_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_type ALTER COLUMN usertype_id SET DEFAULT nextval('public.user_type_usertype_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: administrators; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: staffs; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.staffs (staff_id, first_name, last_name, other_name, gender, email, supervisor_id, department, grade, is_active, is_superuser, created_at, updated_at) VALUES (1, 'string', 'string', 'string', 'string', 'user@example.com', 0, 'string', 0, true, true, '2023-06-19', '2023-06-19');


--
-- Data for Name: user_type; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.users (user_id, email, hashed_password, is_active, is_superuser, created_at, updated_at, reset_password_token, staff_id) VALUES (1, 'user@example.com', '$2b$12$jipqX2pPfiwT5N17pFAWTObiHQeBYaP9sm9nZ5BdtLNzvWPonN8Aa', true, false, '2023-06-19', '2023-06-19', NULL, NULL);


--
-- Name: administrators_admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.administrators_admin_id_seq', 1, false);


--
-- Name: staffs_staff_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.staffs_staff_id_seq', 1, true);


--
-- Name: user_type_usertype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_type_usertype_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, true);


--
-- Name: administrators administrators_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrators
    ADD CONSTRAINT administrators_pkey PRIMARY KEY (admin_id);


--
-- Name: administrators administrators_push_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrators
    ADD CONSTRAINT administrators_push_id_key UNIQUE (push_id);


--
-- Name: staffs staffs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staffs
    ADD CONSTRAINT staffs_pkey PRIMARY KEY (staff_id);


--
-- Name: user_type user_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_type
    ADD CONSTRAINT user_type_pkey PRIMARY KEY (usertype_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: ix_public_administrators_admin_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_public_administrators_admin_id ON public.administrators USING btree (admin_id);


--
-- Name: ix_public_administrators_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_public_administrators_email ON public.administrators USING btree (email);


--
-- Name: ix_staffs_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_staffs_email ON public.staffs USING btree (email);


--
-- Name: ix_staffs_staff_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_staffs_staff_id ON public.staffs USING btree (staff_id);


--
-- Name: ix_user_type_usertype_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_user_type_usertype_id ON public.user_type USING btree (usertype_id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_users_user_id ON public.users USING btree (user_id);


--
-- Name: users users_staff_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES public.staffs(staff_id);


--
-- PostgreSQL database dump complete
--

