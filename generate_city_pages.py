import json
import os
import re

# Define the list of all 87 cities with their details
cities = [
    # Major urban areas
    {"id": "auckland", "name": "Auckland", "description": "Get cash for your car in Auckland today!", "postal": "1010"},
    {"id": "wellington", "name": "Wellington", "description": "Fast car selling service in Wellington.", "postal": "6011"},
    {"id": "christchurch", "name": "Christchurch", "description": "Sell your car for cash in Christchurch.", "postal": "8023"},
    {"id": "hamilton", "name": "Hamilton", "description": "Top dollar for your vehicle in Hamilton.", "postal": "3204"},
    {"id": "tauranga", "name": "Tauranga", "description": "Quick cash for cars in Tauranga.", "postal": "3110"},
    {"id": "napier", "name": "Napier", "description": "Sell your car fast in Napier.", "postal": "4142"},
    {"id": "palmerston-north", "name": "Palmerston North", "description": "Instant cash for cars in Palmerston North.", "postal": "4410"},
    {"id": "nelson", "name": "Nelson", "description": "Get paid today for your car in Nelson.", "postal": "7010"},
    {"id": "rotorua", "name": "Rotorua", "description": "Cash for cars in Rotorua.", "postal": "3120"},
    {"id": "new-plymouth", "name": "New Plymouth", "description": "Sell your car quickly in New Plymouth.", "postal": "4340"},
    {"id": "invercargill", "name": "Invercargill", "description": "Top prices for cars in Invercargill.", "postal": "9812"},
    {"id": "dunedin", "name": "Dunedin", "description": "Fast cash for cars in Dunedin.", "postal": "9016"},
    {"id": "whangarei", "name": "Whangarei", "description": "Sell your car for cash in Whangarei.", "postal": "0110"},
    {"id": "manukau", "name": "Manukau", "description": "Instant payment for your car in Manukau.", "postal": "2104"},
    {"id": "taita", "name": "Taita", "description": "Cash for any car condition in Taita.", "postal": "5011"},
    
    # Other main centers
    {"id": "gisborne", "name": "Gisborne", "description": "Fast cash for cars in Gisborne.", "postal": "4010"},
    {"id": "taupo", "name": "Taupo", "description": "Top dollar for cars in Taupo.", "postal": "3330"},
    {"id": "hastings", "name": "Hastings", "description": "Sell your car in Hastings.", "postal": "4158"},
    {"id": "blenheim", "name": "Blenheim", "description": "Cash for cars in Blenheim.", "postal": "7201"},
    {"id": "timaru", "name": "Timaru", "description": "Top prices for cars in Timaru.", "postal": "7910"},
    {"id": "masterton", "name": "Masterton", "description": "Sell your car fast in Masterton.", "postal": "5810"},
    {"id": "whakatane", "name": "Whakatane", "description": "Fast car selling in Whakatane.", "postal": "3120"},
    {"id": "opotiki", "name": "Opotiki", "description": "Cash for cars in Opotiki.", "postal": "3130"},
    {"id": "te-puke", "name": "Te Puke", "description": "Top dollar for cars in Te Puke.", "postal": "3110"},
    {"id": "kawerau", "name": "Kawerau", "description": "Sell your vehicle in Kawerau.", "postal": "3181"},
    {"id": "wairoa", "name": "Wairoa", "description": "Get cash for your car in Wairoa.", "postal": "4191"},
    {"id": "dannevirke", "name": "Dannevirke", "description": "Top prices for cars in Dannevirke.", "postal": "4951"},
    {"id": "waipukurau", "name": "Waipukurau", "description": "Fast car selling in Waipukurau.", "postal": "4241"},
    {"id": "ashhurst", "name": "Ashhurst", "description": "Cash for cars in Ashhurst.", "postal": "5010"},
    {"id": "featherston", "name": "Featherston", "description": "Sell your car in Featherston.", "postal": "5710"},
    {"id": "carterton", "name": "Carterton", "description": "Top dollar for cars in Carterton.", "postal": "5711"},
    {"id": "martinborough", "name": "Martinborough", "description": "Fast cash for cars in Martinborough.", "postal": "5712"},
    {"id": "renwick", "name": "Renwick", "description": "Cash for cars in Renwick.", "postal": "7605"},
    {"id": "picton", "name": "Picton", "description": "Sell your car in Picton.", "postal": "7220"},
    {"id": "brightwater", "name": "Brightwater", "description": "Top prices for cars in Brightwater.", "postal": "7019"},
    {"id": "richmond", "name": "Richmond", "description": "Fast car selling in Richmond.", "postal": "7020"},
    {"id": "motueka", "name": "Motueka", "description": "Cash for cars in Motueka.", "postal": "7122"},
    {"id": "kaiteriteri", "name": "Kaiteriteri", "description": "Sell your car in Kaiteriteri.", "postal": "7054"},
    {"id": "mapua", "name": "Mapua", "description": "Top dollar for cars in Mapua.", "postal": "7017"},
    {"id": "takaka", "name": "Takaka", "description": "Fast cash for cars in Takaka.", "postal": "7184"},
    {"id": "rewwa", "name": "Reefton", "description": "Cash for cars in Reefton.", "postal": "7830"},
    {"id": "westport", "name": "Westport", "description": "Sell your car in Westport.", "postal": "7820"},
    {"id": "greymouth", "name": "Greymouth", "description": "Top prices for cars in Greymouth.", "postal": "7809"},
    {"id": "hokitika", "name": "Hokitika", "description": "Fast car selling in Hokitika.", "postal": "7880"},
    {"id": "franz-josef", "name": "Franz Josef", "description": "Cash for cars in Franz Josef.", "postal": "7810"},
    {"id": "fox-glacier", "name": "Fox Glacier", "description": "Sell your car in Fox Glacier.", "postal": "7811"},
    {"id": "wanaka", "name": "Wanaka", "description": "Top dollar for cars in Wanaka.", "postal": "9305"},
    {"id": "queenstown", "name": "Queenstown", "description": "Fast cash for cars in Queenstown.", "postal": "9300"},
    {"id": "te-anau", "name": "Te Anau", "description": "Cash for cars in Te Anau.", "postal": "9610"},
    {"id": "manapouri", "name": "Manapouri", "description": "Sell your car in Manapouri.", "postal": "9620"},
    {"id": "thames", "name": "Thames", "description": "Top prices for cars in Thames.", "postal": "3500"},
    {"id": "coromandel", "name": "Coromandel", "description": "Fast cash for cars in Coromandel.", "postal": "3553"},
    {"id": "whitianga", "name": "Whitianga", "description": "Cash for cars in Whitianga.", "postal": "3587"},
    {"id": "mercury-bay", "name": "Mercury Bay", "description": "Sell your car in Mercury Bay.", "postal": "3501"},
    {"id": "katikati", "name": "Katikati", "description": "Top dollar for cars in Katikati.", "postal": "3186"},
    {"id": "te-awamutu", "name": "Te Awamutu", "description": "Fast cash for cars in Te Awamutu.", "postal": "3800"},
    {"id": "kusini", "name": "Kawerau", "description": "Cash for cars in Kawerau.", "postal": "3181"},
    {"id": "turangi", "name": "Turangi", "description": "Sell your car in Turangi.", "postal": "3384"},
    {"id": "ohakune", "name": "Ohakune", "description": "Top prices for cars in Ohakune.", "postal": "4844"},
    {"id": "waiouru", "name": "Waiouru", "description": "Fast cash for cars in Waiouru.", "postal": "4991"},
    {"id": "wanganui", "name": "Wanganui", "description": "Cash for cars in Wanganui.", "postal": "4500"},
    {"id": "waverley", "name": "Waverley", "description": "Sell your car in Waverley.", "postal": "4528"},
    {"id": "taranaki", "name": "Taranaki", "description": "Top dollar for cars in Taranaki.", "postal": "4312"},
    {"id": "inangahua", "name": "Inangahua", "description": "Fast cash for cars in Inangahua.", "postal": "7822"},
    {"id": "reuss", "name": "Reuss", "description": "Cash for cars in Reuss.", "postal": "7831"},
    {"id": "north-land", "name": "Northland", "description": "Sell your car in Northland.", "postal": "0131"},
    {"id": "dargaville", "name": "Dargaville", "description": "Top prices for cars in Dargaville.", "postal": "0380"},
    {"id": "kaitaia", "name": "Kaitaia", "description": "Fast cash for cars in Kaitaia.", "postal": "0410"},
    {"id": "kaikohe", "name": "Kaikohe", "description": "Cash for cars in Kaikohe.", "postal": "0435"},
    {"id": "paihia", "name": "Paihia", "description": "Sell your car in Paihia.", "postal": "0210"},
    {"id": "kerikeri", "name": "Kerikeri", "description": "Top dollar for cars in Kerikeri.", "postal": "0232"},
    {"id": "alexandra", "name": "Alexandra", "description": "Fast cash for cars in Alexandra.", "postal": "9344"},
    {"id": "cromwell", "name": "Cromwell", "description": "Cash for cars in Cromwell.", "postal": "9383"},
    {"id": "lumsden", "name": "Lumsden", "description": "Sell your car in Lumsden.", "postal": "9644"},
    {"id": "gore", "name": "Gore", "description": "Top prices for cars in Gore.", "postal": "9710"},
    {"id": "mataura", "name": "Mataura", "description": "Fast cash for cars in Mataura.", "postal": "9741"},
    {"id": "winton", "name": "Winton", "description": "Cash for cars in Winton.", "postal": "9653"},
    {"id": "stewart-island", "name": "Stewart Island", "description": "Sell your car in Stewart Island.", "postal": "9855"},
    {"id": "otago", "name": "Otago", "description": "Top dollar for cars in Otago.", "postal": "9016"},
    {"id": "southland", "name": "Southland", "description": "Fast cash for cars in Southland.", "postal": "9812"},
    {"id": "buller", "name": "Buller", "description": "Cash for cars in Buller.", "postal": "7812"},
    {"id": "selwyn", "name": "Selwyn", "description": "Sell your car in Selwyn.", "postal": "7609"},
    {"id": "waimakariri", "name": "Waimakariri", "description": "Top prices for cars in Waimakariri.", "postal": "7600"},
    {"id": "rakaia", "name": "Rakaia", "description": "Fast cash for cars in Rakaia.", "postal": "7640"},
    {"id": "ashburton", "name": "Ashburton", "description": "Cash for cars in Ashburton.", "postal": "7700"},
    {"id": "temuka", "name": "Temuka", "description": "Sell your car in Temuka.", "postal": "7912"},
    {"id": "geraldine", "name": "Geraldine", "description": "Top dollar for cars in Geraldine.", "postal": "7930"},
    {"id": "fairlie", "name": "Fairlie", "description": "Fast cash for cars in Fairlie.", "postal": "7952"},
    {"id": "lassen", "name": "Lassen", "description": "Cash for cars in Lassen.", "postal": "7832"},
    {"id": "alpine", "name": "Alpine", "description": "Sell your car in Alpine.", "postal": "7833"},
    {"id": "glencoe", "name": "Glencoe", "description": "Top prices for cars in Glencoe.", "postal": "7834"},
    {"id": "murchison", "name": "Murchison", "description": "Fast cash for cars in Murchison.", "postal": "7835"},
    {"id": "springfield", "name": "Springfield", "description": "Cash for cars in Springfield.", "postal": "7646"},
    {"id": "darwin", "name": "Darwin", "description": "Sell your car in Darwin.", "postal": "7836"},
    {"id": "maruia", "name": "Maruia", "description": "Top dollar for cars in Maruia.", "postal": "7825"},
    {"id": "lyell", "name": "Lyell", "description": "Cash for cars in Lyell.", "postal": "7826"},
    {"id": "reikorangi", "name": "Reikorangi", "description": "Cash for cars in Reikorangi.", "postal": "5810"}
]

# Read the template file
with open('city-template.html', 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()


def generate_enhanced_schema(city_name, city_id, postal_code, latitude, longitude, suburbs_served=None):
    """
    Generate enhanced schema markup for a specific city
    """
    if suburbs_served is None:
        suburbs_served = [city_name]
    
    # Create area served array
    area_served = []
    for suburb in suburbs_served:
        area_served.append({
            "@type": "City",
            "name": suburb
        })
    
    # Convert area served to JSON string
    area_served_json = ",\n    ".join([f'    {{"@type": "City", "name": "{sub}"}}' for sub in suburbs_served])
    
    schema_json = f'''    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Easy Cash for Cars {city_name}",
  "image": "https://easycashforcars.nz/assets/logo.png",
  "@id": "https://easycashforcars.nz/{city_id}.html",
  "url": "https://easycashforcars.nz/{city_id}.html",
  "telephone": "0800-900-018",
  "alternateName": ["Cash for Cars {city_name}", "Sell My Car {city_name}", "{city_name} Car Buyers", "Top Dollar Cars {city_name}", "Scrap Car {city_name}", "Junk Car {city_name}"],
  "priceRange": "$",
  "openingHours": [
    "Mo-Su 08:00-20:00"
  ],
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "77 Francella St",
    "addressLocality": "Bromley",
    "addressRegion": "{city_name}",
    "postalCode": "{postal_code}",
    "addressCountry": "NZ"
  }},
  "geo": {{
    "@type": "GeoCoordinates",
    "latitude": {latitude},
    "longitude": {longitude}
  }},
  "serviceType": ["Car Buying", "Vehicle Purchase", "Cash for Cars", "Car Removal", "Scrap Car Service", "Junk Car Removal", "Salvage Car Buyers", "Instant Car Payment"],
  "areaServed": [
    {area_served_json}
  ],
  "makesOffer": [
    {{
      "@type": "Offer",
      "itemOffered": {{
        "@type": "Service",
        "name": "Cash for Cars {city_name}",
        "description": "We buy any car for cash in {city_name}. Top prices for all makes and models regardless of condition. Free pickup anywhere in {city_name}."
      }},
      "priceSpecification": {{
        "@type": "PriceSpecification",
        "price": "Varies",
        "priceCurrency": "NZD"
      }}
    }}
  ],
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "1000",
    "bestRating": "5",
    "worstRating": "1"
  }},
  "review": [
    {{
      "@type": "Review",
      "reviewBody": "Sold my old car to Easy Cash for Cars and they gave me the best price in {city_name}. Quick process and paid cash on the spot!",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": 5
      }},
      "author": {{
        "@type": "Person",
        "name": "{city_name} Customer"
      }},
      "datePublished": "2023-06-15"
    }}
  ],
  "founder": {{
    "@type": "Person",
    "name": "{city_name} Car Sales Team"
  }},
  "slogan": "Top Dollar for Your Car in {city_name} - Fast, Easy, Reliable!",
  "description": "Get instant cash for your car in {city_name}. We buy any car, truck, van, or SUV regardless of condition. Free pickup and same-day payment in {city_name}.",
  "sameAs": [
    "https://www.facebook.com/easycashforcarsnz",
    "https://www.instagram.com/easycashforcarsnz"
  ]
}}
    </script>'''
    
    return schema_json

# Function to generate FAQ section for a city with schema markup
def generate_faq(city_name):
    faq_html = f'''
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {{
                "@type": "Question",
                "name": "How much can I get for my car in {city_name}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "The value of your car depends on several factors including the make, model, year, condition, and current market demand. We provide free, no-obligation quotes for cars in {city_name}. Contact us with details about your vehicle and we'll give you a fair offer based on current market prices."
                }}
            }},
            {{
                "@type": "Question",
                "name": "Do you buy cars in any condition in {city_name}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "Yes, we buy cars in all conditions, whether they're running or not. This includes damaged vehicles, flood-damaged cars, wrecks, and old/scrapped vehicles. No car is too damaged for us in the {city_name} area."
                }}
            }},
            {{
                "@type": "Question",
                "name": "How quickly can you pick up my car in {city_name}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "We pride ourselves on fast service throughout {city_name}. Once you accept our offer, we can typically arrange collection within 24 hours at a time that suits you, whether at your home or workplace in {city_name}."
                }}
            }},
            {{
                "@type": "Question",
                "name": "What paperwork do I need to sell my car in {city_name}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "To sell your car in {city_name}, you'll need to provide your ID, the vehicle title/registration, and any service records if available. We'll handle all the legal paperwork required to transfer ownership and ensure everything is completed properly."
                }}
            }},
            {{
                "@type": "Question",
                "name": "Do you provide free car removal in {city_name}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "Yes, we provide free car removal throughout the {city_name} area. Once we've made an offer and you've accepted, we'll come to you to collect the vehicle at no additional cost. There's no need to transport the car to us."
                }}
            }}
        ]
    }}
    </script>
    <section id="faq" class="faq">
        <div class="container">
            <h2>Frequently Asked Questions - {city_name}</h2>
            <div class="faq-container">
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>How much can I get for my car in {city_name}?</h3>
                    </div>
                    <div class="faq-answer">
                        <p>The value of your car depends on several factors including the make, model, year, condition, and current market demand. We provide free, no-obligation quotes for cars in {city_name}. Contact us with details about your vehicle and we'll give you a fair offer based on current market prices.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>Do you buy cars in any condition in {city_name}?</h3>
                    </div>
                    <div class="faq-answer">
                        <p>Yes, we buy cars in all conditions, whether they're running or not. This includes damaged vehicles, flood-damaged cars, wrecks, and old/scrapped vehicles. No car is too damaged for us in the {city_name} area.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>How quickly can you pick up my car in {city_name}?</h3>
                    </div>
                    <div class="faq-answer">
                        <p>We pride ourselves on fast service throughout {city_name}. Once you accept our offer, we can typically arrange collection within 24 hours at a time that suits you, whether at your home or workplace in {city_name}.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>What paperwork do I need to sell my car in {city_name}?</h3>
                    </div>
                    <div class="faq-answer">
                        <p>To sell your car in {city_name}, you'll need to provide your ID, the vehicle title/registration, and any service records if available. We'll handle all the legal paperwork required to transfer ownership and ensure everything is completed properly.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>Do you provide free car removal in {city_name}?</h3>
                    </div>
                    <div class="faq-answer">
                        <p>Yes, we provide free car removal throughout the {city_name} area. Once we've made an offer and you've accepted, we'll come to you to collect the vehicle at no additional cost. There's no need to transport the car to us.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''
    return faq_html

# Generate HTML file for each city
for city in cities:
    # Replace placeholders with actual city data
    content = template_content
    
    # Replace city names/IDs
    content = content.replace('[CITY]', city['name'])
    content = content.replace('[City]', city['name'])
    content = content.replace('"addressRegion": "[City]"', '"addressRegion": "' + city['name'] + '"')
    content = content.replace('"postalCode": "[POSTAL_CODE]"', '"postalCode": "' + city['postal'] + '"')
    
    # Update title and meta tags for SEO
    content = content.replace(
        '<title id="pageTitle">Cash for Cars [City] – Sell Your Car Fast & Easy</title>',
        '<title id="pageTitle">Cash for Cars ' + city['name'] + ' – Sell Your Car Fast & Easy</title>'
    )
    
    content = content.replace(
        '<meta name="description" id="pageDescription" content="Looking to sell your car in [City]? Get instant cash today! Fast, reliable, hassle-free car selling service.">',
        '<meta name="description" id="pageDescription" content="Looking to sell your car in ' + city['name'] + '? Get instant cash today! Fast, reliable, hassle-free car selling service in ' + city['name'] + '.">'
    )
    
    content = content.replace(
        '<meta name="keywords" id="pageKeywords" content="cash for cars [City], sell my car [City], car buyers [City], instant car sale [City], scrap car for cash [City]">',
        '<meta name="keywords" id="pageKeywords" content="cash for cars ' + city['name'] + ', sell my car ' + city['name'] + ', car buyers ' + city['name'] + ', instant car sale ' + city['name'] + ', scrap car for cash ' + city['name'] + '">'
    )
    
    # Generate enhanced schema for this city
    # Using default coordinates if not provided in the city data
    latitude = city.get("latitude", -43.5321)  # Default to Christchurch coordinates
    longitude = city.get("longitude", 172.6362)  # Default to Christchurch coordinates
    suburbs = city.get("suburbs", [city['name']])  # Default to just the city name
    postal_code = city.get("postal", "0000")
    
    enhanced_schema = generate_enhanced_schema(city['name'], city['id'], postal_code, latitude, longitude, suburbs)
    
    # Insert the enhanced schema after the opening <head> tag
    content = content.replace('<head>', '<head>\n    ' + enhanced_schema)
    
    # Add FAQ section before the footer
    faq_section = generate_faq(city['name'])
    content = content.replace('    <!-- Footer -->', '    ' + faq_section + '\n    <!-- Footer -->')
    
    # Write the generated HTML to a file
    filename = city['id'] + ".html"
    with open(filename, 'w', encoding='utf-8') as output_file:
        output_file.write(content)
    
    print("Generated: " + filename)

print("\\nSuccessfully generated " + str(len(cities)) + " city pages!")