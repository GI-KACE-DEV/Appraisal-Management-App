--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 14.7 (Ubuntu 14.7-0ubuntu0.22.04.1)

-- Started on 2023-05-16 14:30:16 GMT

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
-- TOC entry 202 (class 1259 OID 82975)
-- Name: staff; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.staff (
    staff_id bigint NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    other_name character varying(255),
    gender character varying(50) NOT NULL,
    supervisor_id integer,
    department character varying(255) NOT NULL,
    grade integer NOT NULL,
    date_joined date NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone
);


--
-- TOC entry 203 (class 1259 OID 82983)
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL,
    username character varying,
    staff_id integer NOT NULL,
    status integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone
);


--
-- TOC entry 2967 (class 0 OID 82975)
-- Dependencies: 202
-- Data for Name: staff; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2968 (class 0 OID 82983)
-- Dependencies: 203
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2837 (class 2606 OID 82982)
-- Name: staff staff_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (id);


--
-- TOC entry 2839 (class 2606 OID 82990)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 2840 (class 2606 OID 82991)
-- Name: users staff_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT staff_id FOREIGN KEY (staff_id) REFERENCES public.staff(id);


-- Completed on 2023-05-16 14:30:17 GMT

--
-- PostgreSQL database dump complete
--

