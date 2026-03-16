import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_presentation():
    prs = Presentation()
    
    # helper for slide with title and bullets
    def add_bullet_slide(title_text, bullets):
        slide_layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(slide_layout)
        title = slide.shapes.title
        title.text = title_text
        
        tf = slide.placeholders[1].text_frame
        tf.text = bullets[0] if bullets else ""
        for bullet in bullets[1:]:
            p = tf.add_paragraph()
            p.text = bullet
            p.level = 0

    # 1. Title Slide
    slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Ernakulam District Analysis"
    subtitle.text = "A roadmap for post-remittance entrepreneurial growth and economic resilience."

    # 2. Geographic & Demographic Profile
    add_bullet_slide("Geographic & Demographic Profile", [
        "Area: 3,068 sq km (Central Kerala)",
        "Kochi: Commercial Capital / Major City",
        "7 Taluks, 13 Municipalities, 1 Municipal Corporation",
        "Coastline: ~46 km along Arabian Sea",
        "Rivers: Periyar, Muvattupuzha, Chalakudy",
        "Islands: Willingdon, Vallarpadam, Vypin"
    ])

    # 3. Context & Remittance
    add_bullet_slide("Economic Context: Remittance Dependency", [
        "Total Population: 3.28M | Literacy: 97.05%",
        "Per Capita Income: ₹94,392 (Pre-milestone)",
        "Gulf Remittance: ₹12,000–15,000 Cr annually",
        "~18% NRI Share; 35% households depend on remittances",
        "High vulnerability to Gulf economic shifts",
        "History: Ancient spice port & colonial trade hub"
    ])

    # 4. Resources & Economic Profile
    add_bullet_slide("Resources & Economic Profile", [
        "Major Industries: Marine/Seafood (2nd largest landing), Coir, Spices, Tourism",
        "GSDP Contribution:",
        "- Services & IT: 42%",
        "- Trade & Logistics: 28%",
        "- Manufacturing: 15%",
        "- Tourism: 8%",
        "- Agriculture/Marine: 7%"
    ])

    # 5. Structural Challenges
    add_bullet_slide("Structural Challenges", [
        "Industrial: High land costs (₹8-15 Cr/acre), MSME tech gap",
        "Employment: Youth unemployment (12.4%), brain drain (60K/year)",
        "Environmental: Flooding vulnerability, coastal erosion",
        "Governance: Single-window delays (90 days), coordination gaps"
    ])

    # 6. SWOT Analysis
    add_bullet_slide("SWOT Analysis", [
        "Strengths: Port-IT synergy, skilled workforce, high literacy",
        "Weaknesses: Unsystematic waste disposal, land constraints",
        "Opportunities: Global maritime corridor, medical tourism, Deep-tech",
        "Threats: Climate/flooding risks, inter-state competition, talent drain"
    ])

    # 7. High Growth Verticals 2040
    add_bullet_slide("High Growth Verticals 2040", [
        "Maritime Economy: Est. ₹25,000 Cr (Container port vision)",
        "Blue Economy: Est. ₹5,000 Cr (Biotech, Seaweed)",
        "IT & Deep Tech: Est. ₹15,000 Cr (Infopark 3.0, AI/ML)",
        "Green Energy: Est. ₹8,000 Cr (Solar/Wind manufacturing)",
        "Medical Tourism: Est. ₹6,000 Cr",
        "Cultural Economy: Est. ₹3,500 Cr (Biennale, Heritage)"
    ])

    # 8. Entrepreneurial Ecosystem
    add_bullet_slide("Entrepreneurial Ecosystem", [
        "EODB: Kerala Rank #13; Sameeksha Online Portal",
        "Components: Kerala Startup Mission (KSUM), Infopark, TiE Kerala",
        "Success Stories:",
        "- FreshToHome ($250M+ funding)",
        "- Entri (10M+ users)",
        "- Genrobotics (Bandicoot robot)"
    ])

    # 9. The Problem: Kochi's Waste Crisis
    add_bullet_slide("Problem: The Waste Crisis", [
        "600+ Tonnes/Day generated; aging infrastructure",
        "Brahmapuram reliance; lack of localized collection",
        "Zero consumer incentive for segregation",
        "Environmental risk to backwaters and livability"
    ])

    # 10. The Solution: GreenBag
    add_bullet_slide("Solution: GreenBag", [
        "App-based waste collection in 30 seconds",
        "Incentive Model: Convert waste into shopping rewards",
        "മാലിന്യം മാറ്റൂ, പോയിന്റുകൾ നേടൂ (Waste to Rewards)",
        "Circular Economy vertical for Ernakulam"
    ])

    # 11. References
    add_bullet_slide("References & Citations", [
        "Kerala State Planning Board (Economic Review 2023-25)",
        "District Industries Centre (DIC) Ernakulam",
        "Kerala Startup Mission (KSUM) Annual Report",
        "Reserve Bank of India (Remittance Data)",
        "KMS 2023 (Migration Survey)"
    ])

    save_path = "Ernakulam_District_Analysis.pptx"
    prs.save(save_path)
    print(f"Presentation saved to {os.path.abspath(save_path)}")

if __name__ == "__main__":
    create_presentation()
