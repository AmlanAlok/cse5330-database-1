-- Q3

-- 3.1	Print the name of state with largest in size
select state
from state 
group by state 
order by max(land_area) desc
limit 1;

-- 3.2	Retrieve the names of counties, their parent state, their population, number of positive cases
-- by date, sorted in the order of highest to lowest density of positive cases per thousand of
-- population.

select c.county, c.state, c.population, cc.positive_count, cc.test_date
from county c
join confirmed_cases cc on c.state = cc.state and c.county = cc.county
order by (cc.positive_count/ c.population)*1000 desc;


-- 3.3	Print similar report as above, but for density of deaths per thousand of population.

select c.county, c.state, c.population, d.death_count, d.report_date
from county c
join deaths d on c.state = d.state and c.county = d.county
order by (d.death_count/ c.population)*1000 desc;

-- 3.4	Show a report for top 10 sensitive counties per state from positive case point of view.

select * from (
select c.state as state, c.county as county, sum(cc.positive_count) as total, ROW_NUMBER() 
over (PARTITION BY state order by sum(cc.positive_count) desc) as rank_no
from county c
join confirmed_cases cc on cc.state = c.state and cc.county = c.county
group by c.state, c.county) rs WHERE rank_no <= 10;

-- 3.5	Print similar report (as 4) from number of death point of view.

select * from (
select c.state as state, c.county as county, sum(d.death_count) as total, ROW_NUMBER() 
over (PARTITION BY state order by sum(d.death_count) desc) as r
from county c
join deaths d on d.county = c.county and c.county = c.county
group by c.state, c.county) rs WHERE r <= 10;

-- 3.6	Prepare a report to show the progress of vaccinations
		-- A.	Sort states by rate of vaccination for 1st dose
select *
from vaccinations v
order by people_with_one_plus_doses_per_100k desc;

		-- B.	Sort states by rate of vaccination for 2nd dose
select *
from vaccinations v
order by people_with_two_plus_doses_per_100k desc;

-- 3.7	Which counties in Texas has at least 5% population have been vaccinated by 1st dose?

select c.county
from vaccinations v
join county c on c.state = v.state
where c.state = 'Texas' and v.people_with_one_plus_doses_per_100k*(c.population/100000) >= (0.05)*c.population;

-- 3.8	Which one county has largest population yet to be vaccinated, considering 75% of population to be vaccinated to achieve herd immunity.

select c.county, max((c.population-v.people_with_one_plus_doses_per_100k*(c.population/100000))) as unvaccinated
from vaccinations v
join county c on c.state = v.state
where c.state = 'Texas' 
group by c.county
order by unvaccinated desc
limit 1;
