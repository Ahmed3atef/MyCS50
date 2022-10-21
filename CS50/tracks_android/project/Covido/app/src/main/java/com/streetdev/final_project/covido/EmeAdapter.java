package com.streetdev.final_project.covido;

import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Filter;
import android.widget.Filterable;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class EmeAdapter extends RecyclerView.Adapter<EmeAdapter.NumberViewHolder> implements Filterable{

    public static class NumberViewHolder extends RecyclerView.ViewHolder{
        public LinearLayout containerView;
        public TextView textView;



        NumberViewHolder(View view){
            super(view);
            containerView = view.findViewById(R.id.num_row);
            textView = view.findViewById(R.id.tv_num_row);

            containerView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    call_numbers current = (call_numbers) containerView.getTag();

                    Intent intent = new Intent(v.getContext(), Country_dial.class);
                    intent.putExtra("name", current.getCountry());
                    intent.putExtra("number", current.getNumber());
                    v.getContext().startActivity(intent);

                }
            });

        }
    }

    public int key = 0;
    private List<call_numbers> filtered = new ArrayList<>();
    private List<call_numbers> callNumbers = Arrays.asList(
            new call_numbers("Egypt","105"),
            new call_numbers( "United State","+202 442 5955"),
            new call_numbers("Canada","+1 833 966 2099"),
            new call_numbers("Saudi Arabia","937"),
            new call_numbers("Algeria","3030"),
            new call_numbers("Angola"," 111"),
            new call_numbers("Republic of Benin","+229 95361104"),
            new call_numbers("Botswana"," +267 3632273"),
            new call_numbers("Burkina Faso","+226 1608989"),
            new call_numbers("Burundi","117"),
            new call_numbers("Cameroon","1510"),
            new call_numbers("Cape Verde","+238 8001112"),
            new call_numbers("Central African Republic","1212"),
            new call_numbers("Chad","1313"),
            new call_numbers("Comoros","+269 4693641"),
            new call_numbers("Côte d’Ivoire","144"),
            new call_numbers("Democratic Republic of Congo","+243 854463582"),
            new call_numbers("Djibouti","1517"),
            new call_numbers("Equatorial Guinea","1111"),
            new call_numbers("Eritrea","+291 7149052"),
            new call_numbers("Eswatini","977"),
            new call_numbers("Ethiopia","8335"),
            new call_numbers("Gabon","1410"),
            new call_numbers("Gambia","1025"),
            new call_numbers("Ghana","+233 509497700"),
            new call_numbers("Guinea","+224 629995656"),
            new call_numbers("Guinea Bissau","1919"),
            new call_numbers("Kenya","719"),
            new call_numbers("Lesotho","+266 58862893"),
            new call_numbers("Liberia","4455"),
            new call_numbers("Libya","191"),
            new call_numbers("Madagascar","910"),
            new call_numbers("Malawi","54747"),
            new call_numbers("Mali","36061"),
            new call_numbers("Mauritania","1155"),
            new call_numbers("Mauritius","8924"),
            new call_numbers("Morocco","+212 0801004747"),
            new call_numbers("Mozambique","84146"),
            new call_numbers("Namibia","0800100100"),
            new call_numbers("Niger","15"),
            new call_numbers("Nigeria","+234 80097000010"),
            new call_numbers("Republic of the Congo","3434"),
            new call_numbers("Rwanda","114"),
            new call_numbers("Sahrawi Republic","+213 664 30 99 86"),
            new call_numbers("Sao Tome and Principe","115"),
            new call_numbers("Senegal","+221 800005050"),
            new call_numbers("Seychelles","141"),
            new call_numbers("Sierra Leone","117"),
            new call_numbers("Somalia","449"),
            new call_numbers("South Africa","0800029999"),
            new call_numbers("South Sudan","6666"),
            new call_numbers("Sudan","9090"),
            new call_numbers("Tanzania","+255 800110124"),
            new call_numbers("Togo","+228 22222073"),
            new call_numbers("Tunisia","190"),
            new call_numbers("Uganda"," +256 800203033"),
            new call_numbers("Zambia","909"),
            new call_numbers("Zimbabwe","+263714734593"),
            new call_numbers("United Kingdom","111"),
            new call_numbers("Germany","112"),
            new call_numbers("Italy", "118"),
            new call_numbers("France","15"),
            new call_numbers("China", "110 "),
            new call_numbers("Oman", "1212")

    );

    @NonNull
    @Override
    public NumberViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.numbers_row, parent, false);

        return  new NumberViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull NumberViewHolder holder, int position) {
        call_numbers current;
        if(key != 0) {
            current = filtered.get(position);
        }
        else{
            current = callNumbers.get(position);
        }

        holder.textView.setText(current.getCountry());
        holder.containerView.setTag(current);

    }

    @Override
    public int getItemCount() {
        if (key != 0){
            return filtered.size();
        }
        else{
            return callNumbers.size();
        }
    }





    private class DialFilter extends Filter{
        @Override
        protected FilterResults performFiltering(CharSequence constraint) {
            // implement your search here!
            FilterResults results = new FilterResults();
            List<call_numbers> filteredDial = new ArrayList<>();

            if((constraint == null) || (constraint.length() == 0)){
                results.values = callNumbers;
                results.count = callNumbers.size();
                key = 0;
            }
            else{
                key = 1;
                for (int i = 0; i < callNumbers.size(); i++){
                    if(callNumbers.get(i).getCountry().toLowerCase().contains(constraint.toString().toLowerCase())){
                        filteredDial.add(callNumbers.get(i));
                    }
                }

                results.values = filteredDial;
                results.count = filteredDial.size();
            }

            return  results;

        }

        @Override
        protected void publishResults(CharSequence constraint, FilterResults results){
            filtered =(List<call_numbers>) results.values;
            notifyDataSetChanged();
        }

    }

    @Override
    public Filter getFilter() {
        return new DialFilter();
    }

}
