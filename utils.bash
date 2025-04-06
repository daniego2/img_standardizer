run_venv (){
    source venv/bin/activate
}

run (){
    python main.py
}

leave_venv (){
    deactivate
}