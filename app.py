{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c789cfee-c6da-43f2-b0d0-176387d4e316",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def login():\n",
    "    return render_template(\"login.html\")\n",
    "\n",
    "@app.route(\"/dashboard\")\n",
    "def dashboard():\n",
    "    # Mock data for preview\n",
    "    buildings = [\"Building A\", \"Building B\"]\n",
    "    selected_building = \"Building A\"\n",
    "    columns = [\"Seat\", \"Employee\"]\n",
    "    seating_data = [{\"id\": 1, \"Seat\": \"101\", \"Employee\": \"Alice\"}, {\"id\": 2, \"Seat\": \"102\", \"Employee\": \"Bob\"}]\n",
    "    return render_template(\"dashboard.html\",\n",
    "                           buildings=buildings,\n",
    "                           selected_building=selected_building,\n",
    "                           columns=columns,\n",
    "                           seating_data=seating_data)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
