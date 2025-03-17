# Ensure you're on the main branch
git checkout main  

# Ensure everything is up to date
git pull origin main  

# Reinstall dependencies locally to ensure correctness
pip install -r requirements.txt  

# Save exact versions of all installed dependencies
pip freeze > requirements.txt  

# Add & commit the updated requirements.txt
git add requirements.txt  
git commit -m "Fixed dependencies and forced reinstall for Streamlit Cloud"  
git push origin main  
