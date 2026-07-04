from flask import Flask, render_template

app = Flask(__name__)

# Master list of parties shown on the hub page.
# A party with "endpoint": None shows as a "coming soon" card instead of a link.
PARTIES = [
    {
        "name": "Labour Party",
        "color": "#E4003B",
        "summary": "Centre-left party, in government following the 2024 general election.",
        "endpoint": "labour",
    },
    {
        "name": "Conservative Party",
        "color": "#0087DC",
        "summary": "Centre-right party, official opposition following the 2024 general election.",
        "endpoint": "conservatives",
    },
    {
        "name": "Liberal Democrats",
        "color": "#FAA61A",
        "summary": "Centrist, pro-European liberal party.",
        "endpoint": "libdems",
    },
    {
        "name": "Reform UK",
        "color": "#12B6CF",
        "summary": "Right-wing populist party led by Nigel Farage.",
        "endpoint": "reformuk",
    },
    {
        "name": "Green Party",
        "color": "#6AB023",
        "summary": "Environmentalist, left-leaning party.",
        "endpoint": "green",
    },
    {
        "name": "Scottish National Party",
        "color": "#FFF95D",
        "summary": "Centre-left party campaigning for Scottish independence.",
        "endpoint": "snp",
    },
    {
        "name": "Plaid Cymru",
        "color": "#005B54",
        "summary": "Centre-left party campaigning for Welsh independence.",
        "endpoint": "plaidcymru",
    },
]


# Neutral, non-party-specific political terms grouped into a few broad categories.
GLOSSARY_TERMS = [
    {"term": "Manifesto", "category": "Elections & Voting",
     "definition": "A document published by a political party before an election, setting out its policies and pledges."},
    {"term": "First-past-the-post (FPTP)", "category": "Elections & Voting",
     "definition": "The electoral system used for UK general elections, where the candidate with the most votes in a constituency wins the seat, even without an outright majority."},
    {"term": "Proportional representation (PR)", "category": "Elections & Voting",
     "definition": "An electoral system where the number of seats a party wins closely reflects the share of votes it received."},
    {"term": "Constituency", "category": "Elections & Voting",
     "definition": "A geographic area represented by one Member of Parliament, elected by the people who live there."},
    {"term": "Marginal seat", "category": "Elections & Voting",
     "definition": "A constituency that could realistically be won by more than one party, often decisive in close elections."},
    {"term": "By-election", "category": "Elections & Voting",
     "definition": "An election held to fill a single seat that becomes vacant between general elections."},
    {"term": "Turnout", "category": "Elections & Voting",
     "definition": "The proportion of eligible voters who actually cast a vote in an election."},
    {"term": "Landslide", "category": "Elections & Voting",
     "definition": "An election result in which one party wins by a very large margin of seats or votes."},

    {"term": "Backbencher", "category": "Parliament & Government",
     "definition": "An MP who does not hold a government minister or opposition frontbench role."},
    {"term": "Frontbencher", "category": "Parliament & Government",
     "definition": "An MP who holds a government minister role, or an opposition spokesperson role."},
    {"term": "Shadow Cabinet", "category": "Parliament & Government",
     "definition": "Senior opposition MPs who each scrutinise, or \"shadow\", a specific government minister's responsibilities."},
    {"term": "Whip", "category": "Parliament & Government",
     "definition": "An MP responsible for making sure party members vote according to party policy; also used to describe the instruction to do so."},
    {"term": "Prime Minister's Questions (PMQs)", "category": "Parliament & Government",
     "definition": "A weekly session in the House of Commons where MPs, including the Leader of the Opposition, question the Prime Minister."},
    {"term": "House of Commons", "category": "Parliament & Government",
     "definition": "The elected lower chamber of the UK Parliament, made up of MPs."},
    {"term": "House of Lords", "category": "Parliament & Government",
     "definition": "The unelected upper chamber of the UK Parliament, made up of appointed and hereditary peers and bishops."},
    {"term": "Coalition government", "category": "Parliament & Government",
     "definition": "A government formed by two or more parties working together, typically because no single party won a majority."},
    {"term": "Hung parliament", "category": "Parliament & Government",
     "definition": "A situation where no single party wins enough seats to have a majority in the House of Commons on its own."},
    {"term": "Cabinet", "category": "Parliament & Government",
     "definition": "The group of senior ministers, chosen by the Prime Minister, who make key government decisions."},
    {"term": "Civil service", "category": "Parliament & Government",
     "definition": "The permanent, politically neutral staff who help implement government policy, regardless of which party is in office."},

    {"term": "Left-wing", "category": "Ideology & Movements",
     "definition": "Broadly associated with support for greater state intervention, redistribution of wealth, and social equality."},
    {"term": "Right-wing", "category": "Ideology & Movements",
     "definition": "Broadly associated with support for free markets, lower taxation, and limited state intervention."},
    {"term": "Centrism", "category": "Ideology & Movements",
     "definition": "A political position that avoids strongly left-wing or right-wing policies, often blending elements of both."},
    {"term": "Populism", "category": "Ideology & Movements",
     "definition": "A political approach that appeals directly to ordinary people, often framing politics as a conflict between \"the people\" and a perceived elite."},
    {"term": "Nationalism", "category": "Ideology & Movements",
     "definition": "A political ideology emphasising the interests, culture, or independence of a particular nation."},
    {"term": "Liberalism", "category": "Ideology & Movements",
     "definition": "A political tradition emphasising individual rights, personal freedoms, and limited government interference."},
    {"term": "Socialism", "category": "Ideology & Movements",
     "definition": "A political and economic ideology advocating collective or state ownership of key industries and resources."},
    {"term": "Conservatism", "category": "Ideology & Movements",
     "definition": "A political tradition emphasising tradition, gradual change, and established institutions."},

    {"term": "Austerity", "category": "Economy & Policy",
     "definition": "Government policy of reducing public spending and borrowing, often introduced during periods of economic difficulty."},
    {"term": "Fiscal policy", "category": "Economy & Policy",
     "definition": "Government decisions about taxation and public spending, used to influence the wider economy."},
    {"term": "National debt", "category": "Economy & Policy",
     "definition": "The total amount of money owed by the government, built up from past borrowing."},
    {"term": "Nationalisation", "category": "Economy & Policy",
     "definition": "Transferring a private industry or company into public, government ownership."},
    {"term": "Means-tested benefit", "category": "Economy & Policy",
     "definition": "Financial support that depends on a person's income or savings, rather than being paid to everyone."},
    {"term": "Net zero", "category": "Economy & Policy",
     "definition": "A target of balancing the amount of greenhouse gas produced with the amount removed from the atmosphere."},

    {"term": "Devolution", "category": "Devolution & Constitution",
     "definition": "The transfer of certain powers from the UK Parliament to national or regional bodies, such as the Scottish Parliament, Senedd, or Northern Ireland Assembly."},
    {"term": "Senedd", "category": "Devolution & Constitution",
     "definition": "The Welsh Parliament, responsible for devolved matters in Wales."},
    {"term": "Scottish Parliament (Holyrood)", "category": "Devolution & Constitution",
     "definition": "The devolved legislature responsible for devolved matters in Scotland."},
    {"term": "Referendum", "category": "Devolution & Constitution",
     "definition": "A public vote on a single specific question, such as independence or EU membership."},
    {"term": "The Union", "category": "Devolution & Constitution",
     "definition": "The political union of England, Scotland, Wales, and Northern Ireland that forms the United Kingdom."},
    {"term": "Independence (in a UK context)", "category": "Devolution & Constitution",
     "definition": "A nation, such as Scotland or Wales, seeking to become a self-governing state separate from the UK."},
]

GLOSSARY_CATEGORIES = [
    "Elections & Voting",
    "Parliament & Government",
    "Ideology & Movements",
    "Economy & Policy",
    "Devolution & Constitution",
]

# Specific laws, schemes, or named policies referenced inside manifesto bullets that a
# general reader may not recognise. Unlike GLOSSARY_TERMS (general political vocabulary,
# shown on its own /glossary page), these are looked up inline on party pages via the
# ref() macro in templates/_macros.html and shown in a popup. Keyed by slug so the same
# concept (e.g. the Barnett formula) can be reused across multiple party pages without
# duplicating the explanation.
REFERENCE_TERMS = {
    "two-child-cap": {
        "title": "Two-child benefit cap",
        "body": "A rule that applied from April 2017 to April 2026, limiting means-tested "
                "benefits such as Universal Credit and Child Tax Credit to a family's first "
                "two children, with some exceptions. It was abolished from 6 April 2026.",
    },
    "rape-clause": {
        "title": "'Rape clause'",
        "body": "The common name for the 'non-consensual conception' exception to the "
                "two-child limit: while that limit applied (2017-2026), it let a parent claim "
                "support for a third or later child conceived through rape or coercive "
                "control, subject to third-party evidence.",
    },
    "barnett-formula": {
        "title": "Barnett formula",
        "body": "A formula used by the UK Treasury to adjust the funding of the Scottish "
                "Government, Welsh Government, and Northern Ireland Executive whenever "
                "spending changes for comparable UK government departments in England, in "
                "proportion to each nation's population.",
    },
    "just-transition": {
        "title": "'Just transition'",
        "body": "A principle that the shift away from fossil fuels should protect the pay, "
                "skills, and job prospects of workers currently employed in affected "
                "industries, such as oil and gas, for example through retraining or support "
                "finding new roles.",
    },
    "non-dom-status": {
        "title": "Non-domiciled ('non-dom') tax status",
        "body": "A tax status, abolished from April 2025, that had let UK residents whose "
                "permanent home was considered to be outside the UK avoid UK tax on foreign "
                "income and gains not brought into the UK. It was replaced by a "
                "residence-based regime, with transitional reliefs for some new arrivals.",
    },
    "border-security-command": {
        "title": "Border Security Command",
        "body": "A law enforcement unit, established in July 2024, that brings together "
                "Border Force, the National Crime Agency, immigration enforcement, and "
                "intelligence agencies to target people-smuggling gangs behind small boat "
                "crossings.",
    },
    "new-deal-working-people": {
        "title": "'New Deal for Working People'",
        "body": "Labour's package of employment law reforms, mostly enacted as the "
                "Employment Rights Act 2025. It introduces day-one rights such as parental "
                "leave and sick pay and restricts 'exploitative' zero-hours contracts, though "
                "unfair-dismissal protection applies after six months rather than from day "
                "one as originally pledged.",
    },
    "rwanda-scheme": {
        "title": "Rwanda scheme",
        "body": "A UK government policy, agreed with Rwanda in 2022, to relocate some people "
                "arriving in the UK without permission (e.g. by small boat) to Rwanda for "
                "asylum processing. It was cancelled by the incoming Labour government in "
                "July 2024, and the underlying treaty was formally terminated in March 2026; "
                "no one was ever compulsorily relocated under it.",
    },
    "triple-lock-plus": {
        "title": "'Triple lock plus'",
        "body": "A Conservative Party pledge at the 2024 general election to apply the state "
                "pension 'triple lock' (increasing by the highest of inflation, average "
                "earnings growth, or 2.5%) to pensioners' tax-free personal allowance too. It "
                "was not implemented after the Conservatives lost the election.",
    },
    "advanced-british-standard": {
        "title": "'Advanced British Standard'",
        "body": "A Conservative Party proposal, announced in 2023, for a single "
                "qualification intended to eventually replace both A-levels and T-levels for "
                "16-18 year-olds in England. It was cancelled by the incoming Labour "
                "government in July 2024 and never introduced.",
    },
    "mortgage-guarantee-scheme": {
        "title": "Mortgage Guarantee Scheme",
        "body": "A UK government scheme, running since 2021 and made permanent from July "
                "2025, in which the government guarantees part of a mortgage to encourage "
                "lenders to offer 91-95% loan-to-value mortgages to buyers with small "
                "deposits.",
    },
    "help-to-buy-scheme": {
        "title": "Help to Buy equity loan scheme",
        "body": "A UK government scheme, open 2013-2023, that offered first-time buyers of "
                "new-build homes a loan for part of the purchase price on top of their "
                "mortgage and deposit. The Conservatives' 2024 manifesto proposed reviving a "
                "new version, but this was not implemented after they lost the election.",
    },
    "commercial-landowner-levy": {
        "title": "Commercial Landowner Levy",
        "body": "A Liberal Democrat proposal, first put forward in 2018, for a tax on the "
                "land value of commercial sites to replace business rates (the current "
                "property-based tax on business premises). It has not been adopted as "
                "government policy.",
    },
    "early-years-pupil-premium": {
        "title": "Early Years Pupil Premium",
        "body": "Ongoing additional funding paid to early years childcare and education "
                "providers in England for each eligible disadvantaged three- or four-year-old "
                "receiving free early education, based on criteria such as family income or "
                "care/adoption history.",
    },
    "echr": {
        "title": "European Convention on Human Rights (ECHR)",
        "body": "An international treaty, overseen by the Council of Europe (a body separate "
                "from and larger than the EU), that protects rights such as a fair trial and "
                "family life across its member states, including the UK.",
    },
    "ir35": {
        "title": "IR35 rules",
        "body": "Tax rules (formally 'off-payroll working rules') designed to identify "
                "contractors who work like employees but bill through their own company, and "
                "to make them pay broadly the same tax and National Insurance as an employee "
                "would.",
    },
}


@app.context_processor
def inject_reference_terms():
    return {"reference_terms": REFERENCE_TERMS}


@app.route("/")
def index():
    return render_template("index.html", parties=PARTIES)


@app.route("/glossary")
def glossary():
    terms = sorted(GLOSSARY_TERMS, key=lambda item: item["term"].lower())
    return render_template("glossary.html", terms=terms, categories=GLOSSARY_CATEGORIES)


@app.route("/labour")
def labour():
    return render_template(
        "labour.html",
        theme="labour",
        theme_color="#E4003B",
        manifesto_url="https://labour.org.uk/change/",
    )


@app.route("/conservatives")
def conservatives():
    return render_template(
        "conservatives.html",
        theme="conservatives",
        theme_color="#0087DC",
        manifesto_url="https://public.conservatives.com/static/documents/GE2024/Conservative-Manifesto-GE2024.pdf",
    )


@app.route("/libdems")
def libdems():
    return render_template(
        "libdems.html",
        theme="libdems",
        theme_color="#FAA61A",
        manifesto_url="https://www.libdems.org.uk/manifesto",
    )


@app.route("/reformuk")
def reformuk():
    return render_template(
        "reformuk.html",
        theme="reformuk",
        theme_color="#12B6CF",
        manifesto_url="https://www.reformparty.uk/our-contract-with-you",
    )


@app.route("/green")
def green():
    return render_template(
        "green.html",
        theme="green",
        theme_color="#6AB023",
        manifesto_url="https://greenparty.org.uk/about/our-manifesto/2024-manifesto-downloads/",
    )


@app.route("/snp")
def snp():
    return render_template(
        "snp.html",
        theme="snp",
        theme_color="#FFF95D",
        manifesto_url="https://s3-eu-west-2.amazonaws.com/www.snp.org/uploads/2024/06/2024-06-20b-SNP-General-Election-Manifesto-2024_interactive.pdf",
    )


@app.route("/plaidcymru")
def plaidcymru():
    return render_template(
        "plaidcymru.html",
        theme="plaidcymru",
        theme_color="#005B54",
        manifesto_url="https://www.partyof.wales/2024",
    )


if __name__ == "__main__":
    app.run(debug=True)
