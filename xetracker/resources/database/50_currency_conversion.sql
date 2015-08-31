CREATE TABLE xetracker.currency_conversion (
    cc_id bigserial,
    cc_provider text NOT NULL,
    cc_currency_from xetracker.iso_currency,
    cc_currency_to xetracker.iso_currency,
    cc_provider_selling_rate numeric(7,5),
    cc_provider_buying_rate numeric(7,5),
    cc_conversion_time timestamp NOT NULL,
    cc_created timestamp NOT NULL DEFAULT now()
);

CREATE UNIQUE 
 INDEX currency_conversion_unique_timestamp_provider_from_to_idx
    ON xetracker.currency_conversion
       (cc_conversion_time,
        cc_provider,
        cc_currency_from,
        cc_currency_to);
