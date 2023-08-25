--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)

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
    email character varying(255),
    is_verified boolean,
    password character varying(255),
    push_id character varying(255) NOT NULL
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
-- Name: appraisal_forms; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.appraisal_forms (
    id integer NOT NULL,
    department character varying(255),
    grade character varying(255),
    positions character varying(255),
    appraisal_year character varying(255),
    staff_id integer,
    supervisor_id integer,
    status boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: appraisal_forms_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.appraisal_forms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: appraisal_forms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.appraisal_forms_id_seq OWNED BY public.appraisal_forms.id;


--
-- Name: apscheduler_jobs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.apscheduler_jobs (
    id character varying(191) NOT NULL,
    next_run_time double precision,
    job_state bytea NOT NULL
);


--
-- Name: department_deadline; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.department_deadline (
    id integer NOT NULL,
    deadline_type character varying(255),
    start_date character varying(255),
    end_date character varying(255),
    deadline_year character varying(255),
    supervisor_id integer,
    comment text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: department_deadline_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.department_deadline_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: department_deadline_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.department_deadline_id_seq OWNED BY public.department_deadline.id;


--
-- Name: email_verication_codes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.email_verication_codes (
    email character varying(255) NOT NULL
);


--
-- Name: end_of_year_review; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.end_of_year_review (
    id integer NOT NULL,
    appraisers_comment_on_workplan text,
    training_development_comments text,
    appraisees_comments_and_plan text,
    head_of_divisions_comments text,
    appraisal_form_id integer,
    performance_details_id integer,
    average_per_rating text,
    average_total text,
    average_per_rating_id text,
    end_status boolean,
    submit boolean,
    approval_status boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: end_of_year_review_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.end_of_year_review_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: end_of_year_review_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.end_of_year_review_id_seq OWNED BY public.end_of_year_review.id;


--
-- Name: messages; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.messages (
    push_id character varying(255) NOT NULL,
    message json NOT NULL,
    web_push_subscription json,
    created timestamp without time zone,
    id integer NOT NULL
);


--
-- Name: messages_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.messages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: messages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.messages_id_seq OWNED BY public.messages.id;


--
-- Name: mid_year_review; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.mid_year_review (
    id integer NOT NULL,
    progress_review text,
    remarks text,
    competency text,
    appraisal_form_id integer,
    deadline_start_date character varying(255),
    deadline_end_date character varying(255),
    mid_status boolean,
    submit_status boolean,
    approval_status boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: mid_year_review_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.mid_year_review_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: mid_year_review_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.mid_year_review_id_seq OWNED BY public.mid_year_review.id;


--
-- Name: overall_performance; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.overall_performance (
    id integer NOT NULL,
    description text,
    performance text,
    status boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: overall_performance_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.overall_performance_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: overall_performance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.overall_performance_id_seq OWNED BY public.overall_performance.id;


--
-- Name: performance_details; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.performance_details (
    id integer NOT NULL,
    comments text,
    approved_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    weight text,
    final_score text,
    appraisal_form_id integer,
    overall_performance_id integer,
    performance_assessment text,
    status boolean,
    submit boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: performance_details_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.performance_details_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: performance_details_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.performance_details_id_seq OWNED BY public.performance_details.id;


--
-- Name: staff_deadline; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.staff_deadline (
    id integer NOT NULL,
    deadline_type character varying(255),
    start_date character varying(255),
    comment text,
    end_date character varying(255),
    deadline_year character varying(255),
    appraisal_form_id integer,
    supervisor_id integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: staff_deadline_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.staff_deadline_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: staff_deadline_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.staff_deadline_id_seq OWNED BY public.staff_deadline.id;


--
-- Name: staffs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.staffs (
    id integer NOT NULL,
    first_name character varying(255),
    last_name character varying(255),
    other_name character varying(255),
    department character varying(255),
    grade character varying(255),
    appointment_date character varying(255),
    gender character varying(255),
    supervisor_id integer,
    positions character varying(255),
    appraisal_form_id integer,
    is_active boolean,
    status boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: staffs_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.staffs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: staffs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.staffs_id_seq OWNED BY public.staffs.id;


--
-- Name: start_of_year; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.start_of_year (
    id integer NOT NULL,
    first_phase text,
    appraisal_form_id integer,
    start_status boolean,
    submit_status boolean,
    approval_status boolean,
    approval_date character varying(255),
    comment text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: start_of_year_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.start_of_year_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: start_of_year_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.start_of_year_id_seq OWNED BY public.start_of_year.id;


--
-- Name: tokens; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tokens (
    id integer,
    access_toke character varying(450) NOT NULL,
    refresh_toke character varying(450) NOT NULL,
    status boolean,
    created_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: user_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_type (
    id integer NOT NULL,
    title character varying(255)
);


--
-- Name: user_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_type_id_seq OWNED BY public.user_type.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(255),
    hashed_password character varying(255),
    is_active boolean,
    is_superuser boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    reset_password_token character varying(255),
    staff_id integer,
    user_type_id integer
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: administrators admin_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrators ALTER COLUMN admin_id SET DEFAULT nextval('public.administrators_admin_id_seq'::regclass);


--
-- Name: appraisal_forms id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.appraisal_forms ALTER COLUMN id SET DEFAULT nextval('public.appraisal_forms_id_seq'::regclass);


--
-- Name: department_deadline id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.department_deadline ALTER COLUMN id SET DEFAULT nextval('public.department_deadline_id_seq'::regclass);


--
-- Name: end_of_year_review id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.end_of_year_review ALTER COLUMN id SET DEFAULT nextval('public.end_of_year_review_id_seq'::regclass);


--
-- Name: messages id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.messages ALTER COLUMN id SET DEFAULT nextval('public.messages_id_seq'::regclass);


--
-- Name: mid_year_review id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mid_year_review ALTER COLUMN id SET DEFAULT nextval('public.mid_year_review_id_seq'::regclass);


--
-- Name: overall_performance id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.overall_performance ALTER COLUMN id SET DEFAULT nextval('public.overall_performance_id_seq'::regclass);


--
-- Name: performance_details id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.performance_details ALTER COLUMN id SET DEFAULT nextval('public.performance_details_id_seq'::regclass);


--
-- Name: staff_deadline id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staff_deadline ALTER COLUMN id SET DEFAULT nextval('public.staff_deadline_id_seq'::regclass);


--
-- Name: staffs id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staffs ALTER COLUMN id SET DEFAULT nextval('public.staffs_id_seq'::regclass);


--
-- Name: start_of_year id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.start_of_year ALTER COLUMN id SET DEFAULT nextval('public.start_of_year_id_seq'::regclass);


--
-- Name: user_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_type ALTER COLUMN id SET DEFAULT nextval('public.user_type_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: administrators; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: appraisal_forms; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: apscheduler_jobs; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: department_deadline; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: email_verication_codes; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: end_of_year_review; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: messages; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: mid_year_review; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: overall_performance; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: performance_details; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: staff_deadline; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: staffs; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: start_of_year; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: tokens; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: user_type; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.user_type (id, title) VALUES (1, 'Admin');
INSERT INTO public.user_type (id, title) VALUES (2, 'Supervisor');
INSERT INTO public.user_type (id, title) VALUES (3, 'Staff');


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Name: administrators_admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.administrators_admin_id_seq', 1, false);


--
-- Name: appraisal_forms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.appraisal_forms_id_seq', 1, false);


--
-- Name: department_deadline_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.department_deadline_id_seq', 1, false);


--
-- Name: end_of_year_review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.end_of_year_review_id_seq', 1, false);


--
-- Name: messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.messages_id_seq', 1, false);


--
-- Name: mid_year_review_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.mid_year_review_id_seq', 1, false);


--
-- Name: overall_performance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.overall_performance_id_seq', 1, false);


--
-- Name: performance_details_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.performance_details_id_seq', 1, false);


--
-- Name: staff_deadline_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.staff_deadline_id_seq', 1, false);


--
-- Name: staffs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.staffs_id_seq', 1, false);


--
-- Name: start_of_year_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.start_of_year_id_seq', 1, false);


--
-- Name: user_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_type_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


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
-- Name: appraisal_forms appraisal_forms_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.appraisal_forms
    ADD CONSTRAINT appraisal_forms_pkey PRIMARY KEY (id);


--
-- Name: apscheduler_jobs apscheduler_jobs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apscheduler_jobs
    ADD CONSTRAINT apscheduler_jobs_pkey PRIMARY KEY (id);


--
-- Name: department_deadline department_deadline_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.department_deadline
    ADD CONSTRAINT department_deadline_pkey PRIMARY KEY (id);


--
-- Name: email_verication_codes email_verication_codes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.email_verication_codes
    ADD CONSTRAINT email_verication_codes_pkey PRIMARY KEY (email);


--
-- Name: end_of_year_review end_of_year_review_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.end_of_year_review
    ADD CONSTRAINT end_of_year_review_pkey PRIMARY KEY (id);


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (id);


--
-- Name: mid_year_review mid_year_review_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mid_year_review
    ADD CONSTRAINT mid_year_review_pkey PRIMARY KEY (id);


--
-- Name: overall_performance overall_performance_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.overall_performance
    ADD CONSTRAINT overall_performance_pkey PRIMARY KEY (id);


--
-- Name: performance_details performance_details_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.performance_details
    ADD CONSTRAINT performance_details_pkey PRIMARY KEY (id);


--
-- Name: staff_deadline staff_deadline_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staff_deadline
    ADD CONSTRAINT staff_deadline_pkey PRIMARY KEY (id);


--
-- Name: staffs staffs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staffs
    ADD CONSTRAINT staffs_pkey PRIMARY KEY (id);


--
-- Name: start_of_year start_of_year_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.start_of_year
    ADD CONSTRAINT start_of_year_pkey PRIMARY KEY (id);


--
-- Name: tokens tokens_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tokens
    ADD CONSTRAINT tokens_pkey PRIMARY KEY (access_toke);


--
-- Name: user_type user_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_type
    ADD CONSTRAINT user_type_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_administrators_admin_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_administrators_admin_id ON public.administrators USING btree (admin_id);


--
-- Name: ix_administrators_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_administrators_email ON public.administrators USING btree (email);


--
-- Name: ix_appraisal_forms_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_appraisal_forms_id ON public.appraisal_forms USING btree (id);


--
-- Name: ix_apscheduler_jobs_next_run_time; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_apscheduler_jobs_next_run_time ON public.apscheduler_jobs USING btree (next_run_time);


--
-- Name: ix_department_deadline_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_department_deadline_id ON public.department_deadline USING btree (id);


--
-- Name: ix_end_of_year_review_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_end_of_year_review_id ON public.end_of_year_review USING btree (id);


--
-- Name: ix_messages_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_messages_id ON public.messages USING btree (id);


--
-- Name: ix_mid_year_review_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_mid_year_review_id ON public.mid_year_review USING btree (id);


--
-- Name: ix_overall_performance_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_overall_performance_id ON public.overall_performance USING btree (id);


--
-- Name: ix_performance_details_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_performance_details_id ON public.performance_details USING btree (id);


--
-- Name: ix_staff_deadline_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_staff_deadline_id ON public.staff_deadline USING btree (id);


--
-- Name: ix_staffs_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_staffs_id ON public.staffs USING btree (id);


--
-- Name: ix_start_of_year_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_start_of_year_id ON public.start_of_year USING btree (id);


--
-- Name: ix_user_type_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_user_type_id ON public.user_type USING btree (id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: appraisal_forms appraisal_forms_staff_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.appraisal_forms
    ADD CONSTRAINT appraisal_forms_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES public.staffs(id);


--
-- Name: appraisal_forms appraisal_forms_supervisor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.appraisal_forms
    ADD CONSTRAINT appraisal_forms_supervisor_id_fkey FOREIGN KEY (supervisor_id) REFERENCES public.staffs(id);


--
-- Name: department_deadline department_deadline_supervisor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.department_deadline
    ADD CONSTRAINT department_deadline_supervisor_id_fkey FOREIGN KEY (supervisor_id) REFERENCES public.staffs(id);


--
-- Name: end_of_year_review end_of_year_review_appraisal_form_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.end_of_year_review
    ADD CONSTRAINT end_of_year_review_appraisal_form_id_fkey FOREIGN KEY (appraisal_form_id) REFERENCES public.appraisal_forms(id);


--
-- Name: end_of_year_review end_of_year_review_performance_details_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.end_of_year_review
    ADD CONSTRAINT end_of_year_review_performance_details_id_fkey FOREIGN KEY (performance_details_id) REFERENCES public.performance_details(id);


--
-- Name: mid_year_review mid_year_review_appraisal_form_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.mid_year_review
    ADD CONSTRAINT mid_year_review_appraisal_form_id_fkey FOREIGN KEY (appraisal_form_id) REFERENCES public.appraisal_forms(id);


--
-- Name: performance_details performance_details_appraisal_form_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.performance_details
    ADD CONSTRAINT performance_details_appraisal_form_id_fkey FOREIGN KEY (appraisal_form_id) REFERENCES public.appraisal_forms(id);


--
-- Name: performance_details performance_details_overall_performance_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.performance_details
    ADD CONSTRAINT performance_details_overall_performance_id_fkey FOREIGN KEY (overall_performance_id) REFERENCES public.overall_performance(id);


--
-- Name: staff_deadline staff_deadline_appraisal_form_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staff_deadline
    ADD CONSTRAINT staff_deadline_appraisal_form_id_fkey FOREIGN KEY (appraisal_form_id) REFERENCES public.appraisal_forms(id);


--
-- Name: staff_deadline staff_deadline_supervisor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staff_deadline
    ADD CONSTRAINT staff_deadline_supervisor_id_fkey FOREIGN KEY (supervisor_id) REFERENCES public.staffs(id);


--
-- Name: staffs staffs_appraisal_form_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.staffs
    ADD CONSTRAINT staffs_appraisal_form_id_fkey FOREIGN KEY (appraisal_form_id) REFERENCES public.appraisal_forms(id);


--
-- Name: start_of_year start_of_year_appraisal_form_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.start_of_year
    ADD CONSTRAINT start_of_year_appraisal_form_id_fkey FOREIGN KEY (appraisal_form_id) REFERENCES public.appraisal_forms(id);


--
-- Name: users users_staff_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES public.staffs(id);


--
-- Name: users users_user_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_user_type_id_fkey FOREIGN KEY (user_type_id) REFERENCES public.user_type(id);


--
-- PostgreSQL database dump complete
--

