
define pronum pro002

define jkcg '借款成功'


block mash_apply_mapping(group_key)
    (
        SELECT
            mash_contract_no,
            max(unique_no) AS unique_no,
            max(apply_no) AS apply_no
        FROM
            loan_front_manager.mf_business_apply
        GROUP BY
            {group_key}
    ) AS mash_apply_mapping
endblock



{% for i in 1,2,3 %}

SELECT
    id,
    mash_apply_mapping.unique_no,
    put_loan_borrowing_no AS loan_no,
    mash_apply_mapping.apply_no,
    '{pronum}' AS product_no,
    {jkcg} AS loan_status,
    NULL AS loan_fial_reason,
    put_loan_amount AS loan_money,
    put_loan_time AS create_time,
    mash_contract_no
FROM
    loan_data_inner.mf_ms_put_loan_account_check
LEFT JOIN {mash_apply_mapping(mash_contract_no)} ON mash_apply_mapping.mash_contract_no = mf_ms_put_loan_account_check.contract_no
WHERE
    unique_no IS NOT NULL
UNION ALL
    SELECT
        *, NULL AS mash_contract_no
    FROM
        loan_front_manager.mf_business_loan_apply_log

{% endfor %}