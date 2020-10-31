--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

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
-- Name: params; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.params (
    id integer,
    name character(1),
    models json
);


ALTER TABLE public.params OWNER TO postgres;

--
-- Name: prices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prices (
    id integer,
    name json
);


ALTER TABLE public.prices OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer,
    name character(1)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: params; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.params (id, name, models) FROM stdin;
\.


--
-- Data for Name: prices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.prices (id, name) FROM stdin;
10000	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name) FROM stdin;
189	В
92	А
\.


--
-- PostgreSQL database dump complete
--

