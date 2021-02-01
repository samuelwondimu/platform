import React from "react";
import { FieldProps } from "formik";
import AsyncSelect from "react-select/async";
import { OptionsType } from "react-select";
import { Option } from "../../types";

// TODO: move to util file
const mapOption = (arr: string[]): Option[] =>
    arr.map((elt) => ({ label: elt, value: elt }));

interface SelectFieldProps extends FieldProps {
    loadOptions: (inputValue: string) => Promise<Option[]>;
}

const SelectField = ({ loadOptions, field, form }: SelectFieldProps) => (
    <AsyncSelect
        cacheOptions
        defaultOptions
        loadOptions={loadOptions}
        name={field.name}
        value={mapOption(field.value)}
        placeholder="Search..."
        isMulti
        onChange={(option: OptionsType<Option>) => {
            form.setFieldValue(
                field.name,
                option.map((item) => item.value)
            );
        }}
        onBlur={field.onBlur}
    />
);

export default SelectField;