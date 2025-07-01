# main.py

import argparse
from soil_detector import detect_soil_type
from recommend import recommend_crops
from map_plot import create_map
from report_generator import generate_pdf_report

def main():
    parser = argparse.ArgumentParser(description="SoilAI - Soil Analysis Tool")
    
    parser.add_argument(
        "--image",
        type=str,
        help="Path to soil image file",
        required=True
    )
    parser.add_argument(
        "--lat",
        type=float,
        help="Latitude of soil sample location",
        required=True
    )
    parser.add_argument(
        "--lon",
        type=float,
        help="Longitude of soil sample location",
        required=True
    )
    
    args = parser.parse_args()
    
    soil_type = detect_soil_type(args.image)
    print(f"Detected soil type: {soil_type}")
    
    recommendations = recommend_crops(soil_type)
    if recommendations:
        crops = recommendations["crops"]
        fertilizers = recommendations["fertilizers"]
        amendments = recommendations["amendments"]
        
        print("Recommended Crops:", crops)
        print("Recommended Fertilizers:", fertilizers)
        print("Organic Amendments:", amendments)
    else:
        print("No recommendations found.")
        return
    
    map_path = "soil_map.html"
    create_map(args.lat, args.lon, soil_type, map_path)
    
    generate_pdf_report(
        soil_type,
        crops,
        fertilizers,
        amendments,
        map_path
    )

if __name__ == "__main__":
    main()
