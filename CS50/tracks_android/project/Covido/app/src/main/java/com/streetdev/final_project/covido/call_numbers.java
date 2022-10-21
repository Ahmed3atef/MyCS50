package com.streetdev.final_project.covido;

public class call_numbers {
    private String country;
    private String number;

    public call_numbers(String country, String number) {
        this.country = country;
        this.number = number;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
}
